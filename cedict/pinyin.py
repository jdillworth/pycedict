# -*- coding: utf-8 -*-
import re


PINYIN_RE = re.compile(r'(([bcdfghjklmnpqrstwxyz]*)'
        r'([aeiouv]+)([bcdfghjklmnpqrstwxyz]*)|r)([1-5])', re.I)


INITIALS_TO_FINALS = {
    '': {
        'a', 'ai', 'an', 'ang', 'ao', 'e', 'ei', 'en', 'eng', 'er', 'o',
        'ou', 'wa', 'wai', 'wan', 'wang', 'wei', 'wen', 'weng', 'wo', 'wu',
        'ya', 'yan', 'yang', 'yao', 'ye', 'yi', 'yin', 'ying', 'yong',
        'you', 'yu', 'yuan', 'yue', 'yun',
    },
    'b': {
        'ba', 'bai', 'ban', 'bang', 'bao', 'bei', 'ben', 'beng', 'bi',
        'bian', 'biao', 'bie', 'bin', 'bing', 'bo', 'bu',
    },
    'c': {
        'ca', 'cai', 'can', 'cang', 'cao', 'ce', 'cei', 'cen', 'ceng',
        'ci', 'cong', 'cou', 'cu', 'cuan', 'cui', 'cun', 'cuo',
    },
    'ch': {
        'cha', 'chai', 'chan', 'chang', 'chao', 'che', 'chen', 'cheng',
        'chi', 'chong', 'chou', 'chu', 'chua', 'chuai', 'chuan', 'chuang',
        'chui', 'chun', 'chuo',
    },
    'd': {
        'da', 'dai', 'dan', 'dang', 'dao', 'de', 'dei', 'den', 'deng', 'di',
        'dian', 'diao', 'die', 'ding', 'diu', 'dong', 'dou', 'du', 'duan',
        'dui', 'dun', 'duo',
    },
    'f': {'fang', 'fo', 'fen', 'fei', 'fan', 'fou', 'fa', 'fu', 'feng'},
    'g': {
        'ga', 'gai', 'gan', 'gang', 'gao', 'ge', 'gei', 'gen', 'geng',
        'gong', 'gou', 'gu', 'gua', 'guai', 'guan', 'guang', 'gui', 'gun',
        'guo',
    },
    'h': {
        'ha', 'hai', 'han', 'hang', 'hao', 'he', 'hei', 'hen', 'heng',
        'hong', 'hou', 'hu', 'hua', 'huai', 'huan', 'huang', 'hui', 'hun',
        'huo',
    },
    'j': {
        'ji', 'jia', 'jian', 'jiang', 'jiao', 'jie', 'jin', 'jing',
       'jiong', 'jiu', 'ju', 'juan', 'jue', 'jun',
    },
    'k': {
        'ka', 'kai', 'kan', 'kang', 'kao', 'ke', 'kei', 'ken', 'keng',
        'kong', 'kou', 'ku', 'kua', 'kuai', 'kuan', 'kuang', 'kui', 'kun',
        'kuo',
    },
    'l': {
        'la', 'lai', 'lan', 'lang', 'lao', 'le', 'lei', 'leng', 'li',
        'lia', 'lian', 'liang', 'liao', 'lie', 'lin', 'ling', 'liu', 'lo',
        'long', 'lou', 'lu', 'lv', 'lve', 'luan', 'lun', 'luo',
    },
    'm': {
        'ma', 'mai', 'man', 'mang', 'mao', 'me', 'mei', 'men', 'meng',
        'mi', 'mian', 'miao', 'mie', 'min', 'ming', 'miu', 'mo', 'mou',
        'mu',
    },
    'n': {
        'nan', 'neng', 'nao', 'nen', 'na', 'nei', 'nang', 'ne', 'nai',
    },
    'p': {
        'pa', 'pai', 'pan', 'pang', 'pao', 'pei', 'pen', 'peng', 'pi',
        'pian', 'piao', 'pie', 'pin', 'ping', 'po', 'pou', 'pu',
    },
    'q': {
        'qi', 'qia', 'qian', 'qiang', 'qiao', 'qie', 'qin', 'qing', 'qiong',
        'qiu', 'qu', 'quan', 'que', 'qun',
    },
    'r': {
        'ran', 'rang', 'rao', 're', 'ren', 'reng', 'ri', 'rong', 'rou',
        'ru', 'rua', 'ruan', 'rui', 'run', 'ruo',
    },
    's': {
        'sa', 'sai', 'san', 'sang', 'sao', 'se', 'sen', 'seng', 'si',
        'song', 'sou', 'su', 'suan', 'sui', 'sun', 'suo',
    },
    'sh': {
        'sha', 'shai', 'shan', 'shang', 'shao', 'she', 'shei', 'shen',
        'sheng', 'shi', 'shou', 'shu', 'shua', 'shuai', 'shuan', 'shuang',
        'shui', 'shun', 'shuo',
    },
    't': {
        'ta', 'tai', 'tan', 'tang', 'tao', 'te', 'teng', 'ti', 'tian', 'tiao',
        'tie', 'ting', 'tong', 'tou', 'tu', 'tuan', 'tui', 'tun', 'tuo',
    },
    'x': {
        'xi', 'xia', 'xian', 'xiang', 'xiao', 'xie', 'xin', 'xing',
        'xiong', 'xiu', 'xu', 'xuan', 'xue', 'xun',
    },
    'z': {
        'za', 'zai', 'zan', 'zang', 'zao', 'ze', 'zei', 'zen', 'zeng', 'zi',
        'zong', 'zou', 'zu', 'zuan', 'zui', 'zun', 'zuo',
    },
    'zh': {
        'zha', 'zhai', 'zhan', 'zhang', 'zhao', 'zhe', 'zhei', 'zhen', 'zheng',
        'zhi', 'zhong', 'zhou', 'zhu', 'zhua', 'zhuai', 'zhuan', 'zhuang', 'zhui',
        'zhun', 'zhuo',
    },
}

TONE_MARKS = {
    'a': '_āáǎàa',
    'e': '_ēéěèe',
    'i': '_īíǐìi',
    'o': '_ōóǒòo',
    'u': '_ūúǔùu',
    'v': '_ǖǘǚǜü',
    'A': '_ĀÁǍÀA',
    'E': '_ĒÉĚÈE',
    'I': '_ĪÍǏÌI',
    'O': '_ŌÓǑÒO',
    'U': '_ŪÚǓÙU',
    'V': '_ǕǗǙǛÜ',
}

SANS_TONE_MARKS = {
    'ā': 'a',
    'á': 'a',
    'ǎ': 'a',
    'à': 'a',
    'a': 'a',
    'ē': 'e',
    'é': 'e',
    'ě': 'e',
    'è': 'e',
    'e': 'e',
    'ī': 'i',
    'í': 'i',
    'ǐ': 'i',
    'ì': 'i',
    'i': 'i',
    'ō': 'o',
    'ó': 'o',
    'ǒ': 'o',
    'ò': 'o',
    'o': 'o',
    'ū': 'u',
    'ú': 'u',
    'ǔ': 'u',
    'ù': 'u',
    'u': 'u',
    'ǖ': 'v',
    'ǘ': 'v',
    'ǚ': 'v',
    'ǜ': 'v',
    'ü': 'v',
    'Ā': 'A',
    'Á': 'A',
    'Ǎ': 'A',
    'À': 'A',
    'A': 'A',
    'Ē': 'E',
    'É': 'E',
    'Ě': 'E',
    'È': 'E',
    'E': 'E',
    'Ī': 'I',
    'Í': 'I',
    'Ǐ': 'I',
    'Ì': 'I',
    'I': 'I',
    'Ō': 'O',
    'Ó': 'O',
    'Ǒ': 'O',
    'Ò': 'O',
    'O': 'O',
    'Ū': 'U',
    'Ú': 'U',
    'Ǔ': 'U',
    'Ù': 'U',
    'U': 'U',
    'Ǖ': 'V',
    'Ǘ': 'V',
    'Ǚ': 'V',
    'Ǜ': 'V',
    'Ü': 'V',
}

ALL_SOUNDS = set(['a', 'ai', 'an', 'ang', 'ao', 'ba', 'bai', 'ban', 'bang',
    'bao', 'bei', 'ben', 'beng', 'bi', 'bian', 'biao', 'bie', 'bin', 'bing',
    'bo', 'bu', 'ca', 'cai', 'can', 'cang', 'cao', 'ce', 'cen', 'ceng', 'cha',
    'chai', 'chan', 'chang', 'chao', 'che', 'chen', 'cheng', 'chi', 'chong',
    'chou', 'chu', 'chuai', 'chuan', 'chuang', 'chui', 'chun', 'chuo', 'ci',
    'cong', 'cou', 'cu', 'cuan', 'cui', 'cun', 'cuo', 'da', 'dai', 'dan',
    'dang', 'dao', 'de', 'dei', 'den', 'deng', 'di', 'dian', 'diao', 'die',
    'ding', 'diu', 'dong', 'dou', 'du', 'duan', 'dui', 'dun', 'duo', 'e', 'en',
    'er', 'fa', 'fan', 'fang', 'fei', 'fen', 'feng', 'fo', 'fou', 'fu', 'ga',
    'gai', 'gan', 'gang', 'gao', 'ge', 'gei', 'gen', 'geng', 'gong', 'gou',
    'gu', 'gua', 'guai', 'guan', 'guang', 'gui', 'gun', 'guo', 'ha', 'hai',
    'han', 'hang', 'hao', 'he', 'hei', 'hen', 'heng', 'hong', 'hou', 'hu',
    'hua', 'huai', 'huan', 'huang', 'hui', 'hun', 'huo', 'ji', 'jia', 'jian',
    'jiang', 'jiao', 'jie', 'jin', 'jing', 'jiong', 'jiu', 'ju', 'juan', 'jue',
    'jun', 'ka', 'kai', 'kan', 'kang', 'kao', 'ke', 'ken', 'keng', 'kong',
    'kou', 'ku', 'kua', 'kuai', 'kuan', 'kuang', 'kui', 'kun', 'kuo', 'la',
    'lai', 'lan', 'lang', 'lao', 'le', 'lei', 'leng', 'li', 'lia', 'lian',
    'liang', 'liao', 'lie', 'lin', 'ling', 'liu', 'long', 'lou', 'lu', 'luan',
    'lun', 'luo', 'lv', 'lvan', 'lve', 'ma', 'mai', 'man', 'mang', 'mao',
    'me', 'mei', 'men', 'meng', 'mi', 'mian', 'miao', 'mie', 'min', 'ming',
    'miou', 'mo', 'mou', 'mu', 'na', 'nai', 'nan', 'nang', 'nao', 'ne', 'nei',
    'nen', 'neng', 'ni', 'nian', 'niang', 'niao', 'nie', 'nin', 'ning', 'niu',
    'nong', 'nou', 'nu', 'nuan', 'nuo', 'nv', 'nve', 'ou', 'pa', 'pai', 'pan',
    'pang', 'pao', 'pei', 'pen', 'peng', 'pi', 'pian', 'piao', 'pie', 'pin',
    'ping', 'po', 'pou', 'pu', 'qi', 'qia', 'qian', 'qiang', 'qiao', 'qie',
    'qin', 'qing', 'qiong', 'qiu', 'qu', 'quan', 'que', 'qun', 'r', 'ran',
    'rang', 'rao', 're', 'ren', 'reng', 'ri', 'rong', 'rou', 'ru', 'ruan',
    'rui', 'run', 'ruo', 'sa', 'sai', 'san', 'sang', 'sao', 'se', 'sen', 'seng',
    'sha', 'shai', 'shan', 'shang', 'shao', 'she', 'shei', 'shen', 'sheng',
    'shi', 'shou', 'shu', 'shua', 'shuai', 'shuan', 'shuang', 'shui', 'shun',
    'shuo', 'si', 'song', 'sou', 'su', 'suan', 'sui', 'sun', 'suo', 'ta', 'tai',
    'tan', 'tang', 'tao', 'te', 'teng', 'ti', 'tian', 'tiao', 'tie', 'ting',
    'tong', 'tou', 'tu', 'tuan', 'tui', 'tun', 'tuo', 'wa', 'wai', 'wan',
    'wang', 'wei', 'wen', 'weng', 'wo', 'wu', 'xi', 'xia', 'xian', 'xiang',
    'xiao', 'xie', 'xin', 'xing', 'xiong', 'xiu', 'xu', 'xuan', 'xue', 'xun',
    'ya', 'yan', 'yang', 'yao', 'ye', 'yi', 'yin', 'ying', 'yong', 'you', 'yu',
    'yuan', 'yue', 'yun', 'za', 'zai', 'zan', 'zang', 'zao', 'ze', 'zen',
    'zeng', 'zha', 'zhai', 'zhan', 'zhang', 'zhao', 'zhe', 'zhen', 'zheng',
    'zhi', 'zhong', 'zhou', 'zhu', 'zhua', 'zhuai', 'zhuan', 'zhuang', 'zhui',
    'zhun', 'zhuo', 'zi', 'zong', 'zou', 'zu', 'zuan', 'zui', 'zun', 'zuo'])

AMBIGUOUS_SOUND_SPELLINGS = {
    'bian': 'bi an',
    'bie': 'bi e',
    'dian': 'di an',
    'diao': 'di ao',
    'die': 'di e',
    'guan': 'gu an',
    'jian': 'ji an',
    'jiang': 'ji ang',
    'jiao': 'ji ao',
    'jie': 'ji e',
    'jue': 'ju e',
    'kuai': 'ku ai',
    'lian': 'li an',
    'liang': 'li ang',
    'liao': 'li ao',
    'luan': 'lu an',
    'miou': 'mi ou',
    'qian': 'qi an',
    'qie': 'qi e',
    'shuan': 'shu an',
    'tian': 'ti an',
    'tuan': 'tu an',
    'xian': 'xi an',
    'xie': 'xi e',
    'yuan': 'yu an',
    'yue': 'yu e',
    'zuan': 'zu an',
}


SOUNDS_BY_LEN = {}
for s in ALL_SOUNDS:
    SOUNDS_BY_LEN.setdefault(len(s), set()).add(s)


def pinyinize(src, raise_exception=False):
    "Turns a source string like 'ni3 hao3' into a utf-8 equivalent with tone marks"

    src = src.replace('u:', 'v')

    try:
        def replacer(m):
            syllable, pre, vowels, post, tone = m.groups()
            vowels = list(vowels)

            if syllable.lower() == 'r' and tone == '5':
                return syllable

            tone = int(tone)

            v = [c.lower() for c in vowels]
            # 3 rules
            # 1- A and E get the tone mark if either one present (they are never both present)
            # 2- in ou, o gets the tone mark
            # 3- in all other cases, last vowel gets the tone
            # see http://pinyin.info/rules/where.html

            # rule 1
            if 'a' in v:
                tindex = v.index('a')
            elif 'e' in v:
                tindex = v.index('e')
            elif ['o', 'u'] == v:  # rule 2
                tindex = 0
            else:  # rule 3
                tindex = len(v) - 1

            try:
                vowels = [
                    v if idx == tindex else TONE_MARKS[v][5]
                    for idx, v in enumerate(vowels)]
                vowels[tindex] = TONE_MARKS[vowels[tindex]][tone]

                vowels = u''.join(vowels)
                return "%s%s%s" % (pre, vowels, post)
            except:  # noqa
                # import sys
                # import traceback
                # typ, err, tb = sys.exc_info()
                # traceback.print_tb(tb)
                # print typ, err
                if raise_exception:
                    raise
                return m.group(0)

        return PINYIN_RE.sub(replacer, src)
    except:  # noqa
        # import sys
        # import traceback
        # typ, err, tb = sys.exc_info()
        # traceback.print_tb(tb)
        # print typ, err, 'src=', repr(src)
        if raise_exception:
            raise

        return src


def depinyinize(src):
    "Turns a source string like 'nǐ hǎo' into 'ni3 hao3'"

    src_sans_tones = ''.join([SANS_TONE_MARKS.get(c, c) for c in list(src)])
    tones_found = len([ch for idx, ch in enumerate(src) if ch != src_sans_tones[idx]])

    if ' ' in src:
        syllables = ' '.join(src_sans_tones.split())
        spacer = ' '
    else:
        spacer = ''
        syllables = []
        syllabizations = syllabize(src_sans_tones)
        tone_count_matches = [s for s in syllabizations if len(s.split()) == tones_found]
        if tone_count_matches:
            syllabizations = tone_count_matches

        # we'll use the first syllabization with no fragment on the end
        for syllabization in syllabizations:
            # was the end a fragment, if so don't use this
            if syllabization.split()[-1].lower() not in ALL_SOUNDS:
                continue

            syllables = syllabization
            break

    if not syllables:
        return src

    src = src.replace(' ', '')
    result = []
    for syllable in syllables.split():
        src_syllable = src[:len(syllable)]
        src = src[len(syllable):]

        tone = ''
        for ch in src_syllable:
            # look for char with tone mark, it won't match its sans-tone self
            no_tone = SANS_TONE_MARKS.get(ch, ch)
            alternative_match = TONE_MARKS[no_tone][5] if no_tone in TONE_MARKS else ch
            if ch not in (no_tone, alternative_match):
                tone = str(TONE_MARKS[no_tone].index(ch))
                result.append(no_tone)
            else:
                result.append(no_tone)

        result.append(tone)
        result.append(spacer)

    return ''.join(result).rstrip()


def _find_syllabizations_from(so_far, full_pinyin, neutral_tone_by_default):
    syllabizations = []

    remainder = full_pinyin[len(''.join(so_far)):]

    if remainder:
        found_sound = False
        for sound in ALL_SOUNDS:
            if remainder.lower()[:len(sound)] == sound:
                found_sound = True
                to_try = [[remainder[:len(sound)]]]
                if sound in AMBIGUOUS_SOUND_SPELLINGS:
                    to_try.append(AMBIGUOUS_SOUND_SPELLINGS[sound].split())

                if len(remainder) > len(sound) and remainder[len(sound)] in '12345':
                    for i in range(len(to_try)):
                        to_try[i][-1] += remainder[len(sound)]

                for trial in to_try:
                    syllabizations += _find_syllabizations_from(
                        so_far + tuple(trial),
                        full_pinyin,
                        neutral_tone_by_default,
                    )
        if not found_sound:
            if any(s[:len(remainder)] == remainder.lower() for s in ALL_SOUNDS):
                so_far += (remainder,)
                return [so_far]
            else:
                return []
    else:
        return [so_far]

    return syllabizations


def syllabize(pinyin, neutral_tone_by_default=False):
    pinyin = pinyin.replace(' ', '')

    # find all founds that appear at the front
    valid_syllabifications = _find_syllabizations_from(
        (), pinyin, neutral_tone_by_default)

    valid_syllabifications = list(set([' '.join(s) for s in valid_syllabifications]))
    valid_syllabifications.sort()

    return tuple(valid_syllabifications)
