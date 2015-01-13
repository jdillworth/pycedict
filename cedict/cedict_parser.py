import os, gzip, re

CEDICT_LINE_REGEX = re.compile(ur'^(.*?)\s+(.*?)\s+\[(.*?)\]\s*(/.*/)\s*$', re.IGNORECASE)

VARIANT_DEF_REGEX = re.compile(
    ur'(?P<vartype>\w+)?\s*'
    ur'(variant of|see also)\s*'
    ur'(?P<ch>[^\\[a-z0-9\]\("]+?)\s*'
    ur'(?P<chs>\|[^\\[a-z0-9\]\("]+?)?\s*'
    ur'(?P<py>\[[-a-z0-9,: ]+\])?$', re.IGNORECASE)

def _find_variants(defs):
    defs2 = []
    variants = []
    for d in defs:
        m = VARIANT_DEF_REGEX.search(d)
        if not m:
            defs2.append(d)
        else:
            v = m.groupdict('')
            if v['chs']: # chop off |
                v['chs'] = v['chs'][1:]
            else: # if no chs specified, same as ch
                v['chs'] = v['ch']

            if v['py']:# chop off [ ]
                v['py'] = v['py'][1:-1]

            # see if there is anything invalid

            # non-chinese in chinese
            if any((ord(c) < 128 and c != ' ') for c in (v['ch'] + v['chs'])):
                # latin non-space not allowed in chinese
                continue

            # unusual characters in pinyin
            if any(ord(c) >= 128 for c in v['py']):
                # non-latin not allowed in pinyin
                continue

            # unusual characters in vartype
            if any(ord(c) >= 128 for c in v['vartype']):
                # non-latin not allowed in vartype
                continue

            variants.append(v)

    return defs2, variants


def _find_measure_words(chs, pinyin, defs):
    """
    Scans defs for 'CL:' prefixed records (classifier), updates the
    all_measure_words dictionary so that each key is (chs, ch, pinyin)
    and the value is a list of tuple of (chs, pinyin).
    """
    mwords = []
    defs2 = []
    for d in defs:
        if d[:3] != 'CL:':
            defs2.append(d)
        else:
            for mw in d[3:].split(','):
                m = re.search(ur'([^\|]+)(\|.+)?\[(.+)\]', mw)
                if m is None:
                    # did not match???

                    m = re.search(ur'([^\|]+)(\|.+)?', mw)
                    if not m:
                        # failed again without pinyin, giving up
                        continue

                    trad, simp = m.groups()
                    py = None

                else:
                    trad, simp, py = m.groups()

                if not simp:
                    simp = trad
                else:
                    simp = simp[1:] # chop off pipe character

                mwords.append((trad, simp, py))


    return defs2, mwords



def iter_cedict(fileobj):
    """
    Iterate over the lines of a cedict file, yielding a tuple
    for each line as
    (chinese-traditional, chinese-simplified, pinyin, definitions, variants, measure-words)
    """
    for linenumber, line in enumerate(fileobj):
        line = line.strip()

        # skip comments
        if re.search(r'^\s*#', line): continue

        m = CEDICT_LINE_REGEX.search(line.decode('utf-8'))
        if not m:
            continue

        ch, chs, num_pinyin, defs = m.groups()

        # translate u: into v
        defs = re.sub(ur'u:(\w)', ur'v\1', defs)
        num_pinyin = re.sub(ur'u:(\w)', ur'v\1', num_pinyin)

        defs = defs[1:-1].split('/')
        defs, mwords = _find_measure_words(chs, num_pinyin, defs)
        defs, variants = _find_variants(defs)

        yield ch, chs, num_pinyin, defs, variants, mwords
