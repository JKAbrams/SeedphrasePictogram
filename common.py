#!/usr/bin/env python3

import os
import json
import sys

# Wordnet language definitions are a bit wired
wordnet_language_names = {
    'albanian': 'als',
    'arabic': 'arb',
    'bahasa': 'msa',
    'basque': 'eus',
    'bulgarian': 'bul',
    'catalan': 'cat',
    'chinese_simplified': 'cmn',
    'croatian': 'hrv',
    'danish': 'dan',
    'dutch': 'nld',
    'english': 'eng',
    'greek': 'ell',
    'finish': 'fin',
    'french': 'fra',
    'galician': 'glg',
    'hebrew': 'heb',
    'icelandic': 'isl',
    'indonesian': 'ind',
    'italian': 'ita',  # Two of this!
    'japanese': 'jpn',
    'lithuanian': 'lit',
    'malaysian': 'zsm',
    'norwegian_bokmal': 'nob',
    'norwegian_nynorsk': 'nno',
    'polish': 'pol',
    'portuguese': 'por',
    'romanian': 'ron',
    'slovak': 'slk',
    'slovenian': 'slv',
    'spanish': 'spa',
    'swedish': 'swe',
    'thai': 'tha'
}


# Classes used in these .json files, extendet from wordnet classes
word_classes = {
    # From wordent:
    'a': 'adjective',  # wn.ADJ
    's': 'satellite adjective',  # wn.ADJ_SAT
    'r': 'adverb',  # wn.ADV
    'n': 'noun',  # wn.NOUN
    'v': 'verb',  # wn.VERB
    # From complimentary dictionary
    'p': 'preposition',
    'c': 'conjunction',
    'o': 'pronoun',
    'd': 'determiner',
    'i': 'interjection'
}


# Load json file as dictionary, return that dictionary
def loadJson(filename):
    d = {}
    try:
        with open(filename) as f:
            d = json.load(f)
    except IOError:
        pass
    return d


# Saves the dictionary {d} as a json file with name {filename}
# Writes compact (single line) arrays if compatArrays is set
def saveJson(d, filename, compatArrays=False):
    # Override to write a more compact .json file where the arrays are written on the same line
    # Using solution from: https://stackoverflow.com/questions/10097477/python-json-array-newlines
    indent = 2
    if compatArrays:
        if sys.version_info.major == 3 and 4 <= sys.version_info.minor <= 10:
            import _make_iterencode
            json.encoder._make_iterencode = _make_iterencode._make_iterencode
            indent = (2, None)

    with open(filename, "w") as f:
        json.dump(d, f, indent=indent, sort_keys=True)
    print('Wrote %s' % filename)


# Create a complete os independent file location
def mkpath(path, filename, suffix):
    return "%s/%s%s" % (os.path.join(os.path.dirname(__file__), path), filename, suffix)


# Writes string {contents} to file {filename}
# Overwrites if a file of that name exists
def writeFile(filename, contents):
    with open(filename, 'w') as the_file:
        the_file.write(contents)
