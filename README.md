# PyCEDict

A library made for working with [CC-CEDICT](http://cc-cedict.org/wiki/) and
pinyin.

## Installation

  pip install pycedict

## Quick Start

Download CC-CEDICT and gunzip it, save as cedict.txt.


    $ python
    ...
    >>> import cedict
    >>> infile = open('cedict.txt')
    >>> for ch, chs, pinyin, defs, variants, mw in cedict.iter_cedict(infile):
    ...     print chs, pinyin, defs # or probably load this info into your database

iter_cedict will parse "CL:" (classifier/measure word) and "see also" entries
in cedict and provide this information in the variants and mw variables above,
respectively.

You can also add tone marks to pinyin with tone numbers (or remove the tone marks)

    >>> print cedict.pinyinize('ni3hao3')
    nǐhǎo
    >>> print cedict.depinyinize('nǐhǎo')
    ni3hao3
