# -*- coding: utf-8 -*-

import unittest
from io import StringIO
from cedict.cedict_parser import iter_cedict
from cedict.pinyin import depinyinize, pinyinize, syllabize

try:
    unicode('hi')
except NameError:
    def unicode(s, encoding):
        return s


SAMPLE_CEDICT = unicode("""齡 龄 [ling2] /age/length of experience, membership etc/
齢 齢 [ling2] /Japanese variant of 齡|龄/
咬 咬 [yao3] /to bite/to nip/
齩 咬 [yao3] /variant of 咬[yao3]/
三氯化磷 三氯化磷 [san1 lu:4 hua4 lin2] /phosphorous trichloride/
麵包房 面包房 [mian4 bao1 fang2] /bakery/CL:家[jia1]/
鮎 鲇 [nian2] /sheatfish (Parasilurus asotus)/oriental catfish/see also 鯰|鲶[nian2]/
鯰 鲶 [nian2] /sheatfish (Parasilurus asotus)/oriental catfish/see also 鮎|鲇[nian2]/""", 'utf-8')


class TestIterCEDict(unittest.TestCase):
    def setUp(self):
        self.f = StringIO(SAMPLE_CEDICT)

    def test_pinyin_correct(self):
        entries = {}
        for ch, chs, pinyin, defs, variants, mw in iter_cedict(self.f):
            entries[chs] = pinyin

        self.assertEqual(entries[u'三氯化磷'], 'san1 lv4 hua4 lin2')
        self.assertEqual(entries[u'面包房'], 'mian4 bao1 fang2')
        self.assertEqual(entries[u'鲇'], 'nian2')

    def test_find_entries(self):
        entries = []
        for ch, chs, pinyin, defs, variants, mw in iter_cedict(self.f):
            entries.append(pinyin)

        self.assertEqual(8, len(entries))
        self.assertEqual('ling2 ling2 yao3 yao3 san1 lv4 '
            'hua4 lin2 mian4 bao1 fang2 nian2 nian2', ' '.join(entries))

    def test_defs_correct(self):
        d = {}
        for ch, chs, pinyin, defs, variants, mw in iter_cedict(self.f):
            d[ch] = defs

        self.assertEqual(d[u'咬'], ['to bite', 'to nip'],
                'should find 2 defs')
        self.assertEqual(d[u'齩'], [],
                'Variant notes are not definitions')
        self.assertEqual(d[u'麵包房'], ['bakery'],
                'Measure words should be removed from definitions')

    def test_measure_words_correct(self):
        d = {}
        for ch, chs, pinyin, defs, variants, mw in iter_cedict(self.f):
            d[ch] = mw

        self.assertEqual(d[u'麵包房'], [(u'家', u'家', u'jia1')],
                'This entry should have a measure word')
        self.assertEqual(len(d[u'鯰']), 0,
                'There is no measure word')

    def test_variants_correct(self):
        d = {}
        for ch, chs, pinyin, defs, variants, mw in iter_cedict(self.f):
            d[ch] = variants


class TestPinyin(unittest.TestCase):

    def test_syllabize_pinyin(self):
        self.assertEqual(syllabize('xi3huan1'), ('xi3 huan1',))
        self.assertEqual(syllabize('nve4dai4'), ('nve4 dai4',))
        self.assertEqual(syllabize('dax'), ('da x',))
        self.assertEqual(syllabize('nizuij'), ('ni zui j',))
        self.assertEqual(syllabize('nizuiji'), ('ni zui ji',))
        self.assertEqual(syllabize('xixixiangg'), ('xi xi xiang g',))
        self.assertEqual(syllabize('xianbian'), (
            'xi an bi an',
            'xi an bian',
            'xian bi an',
            'xian bian',
        ))

    def test_pinyinize(self):
        self.assertEqual(pinyinize('xi3huan1'), u'xǐhuān')
        self.assertEqual(pinyinize('xing2 dong4'), u'xíng dòng')
        self.assertEqual(pinyinize('ni3 hao3'), u'nǐ hǎo')
        self.assertEqual(pinyinize('ni3 hao5'), u'nǐ hao')
        self.assertEqual(pinyinize('hua4'), u'huà')
        self.assertEqual(pinyinize('you3'), u'yǒu')

        # make sure case is preserved
        self.assertEqual(pinyinize('xi3HUan1'), u'xǐHUān')

    def test_depinyinize(self):
        self.assertEqual('xi3huan1', depinyinize(u'xǐhuān'))
        self.assertEqual('xing2 dong4', depinyinize(u'xíng dòng'))
        self.assertEqual('ni3 hao3', depinyinize(u'nǐ hǎo'))
        self.assertEqual('ni3 hao', depinyinize(u'nǐ hao'))
        self.assertEqual('hua4', depinyinize(u'huà'))
        self.assertEqual('you3', depinyinize(u'yǒu'))

        # make sure case is preserved
        self.assertEqual('xi3HUan1', depinyinize(u'xǐHUān'))

    def test_double_dot(self):
        self.assertEqual(pinyinize('nve4dai4'), u'nüèdài')
        self.assertEqual(pinyinize('lu:4fa3'), u'lǜfǎ')

        self.assertEqual(pinyinize('lu:4fa3'), u'lǜfǎ')

        self.assertEqual(pinyinize('nu:e4dai4'), u'nüèdài')

        self.assertEqual(pinyinize('lv4fa3'), u'lǜfǎ')
        self.assertEqual('lv4fa3', depinyinize(u'lǜfǎ'))

        self.assertEqual(pinyinize('lv4fa3'), u'lǜfǎ')
        self.assertEqual('lv4fa3', depinyinize(u'lǜfǎ'))

        self.assertEqual(pinyinize('nve4dai4'), u'nüèdài')
        self.assertEqual('nve4dai4', depinyinize(u'nüèdài'))


if __name__ == '__main__':
    unittest.main()
