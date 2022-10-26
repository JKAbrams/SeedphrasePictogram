#!/usr/bin/env python3

from nltk.corpus import wordnet as wn
import json
import common as cm
from pathlib import Path, PurePath

used_language = 'all'


# Build dictionary
def buildDictionary(wordlist, language):
    dictionary = {}
    filename = cm.mkpath('dictionary', language, '_complementary.json')
    complimentary = cm.loadJson(filename)
    if complimentary == {}:
        print('No complimentary dictionary found for %s' % language)
    else:
        print('Loaded complimentary dictionary %s' % filename)

    for word in wordlist:
        arr = []
        if language in cm.wordnet_language_names:
            # loop through wn for this word
            for cls in wn.synsets(word, lang=cm.wordnet_language_names[language]):
                arr.append([cls.pos(), cls.definition()])
        # if it did not exist, look in the complimentary dictionary
        if not arr:
            if word in complimentary:
                arr = complimentary[word]
        dictionary[word] = arr
    return dictionary


# Load wordlist, returns the wordlist as an array
def loadWordlist(language):
    wordlist_filename = cm.mkpath('wordlist', language, '.txt')
    with open(wordlist_filename, 'r', encoding='utf-8') as f:
        wl = [w.strip() for w in f.readlines()]
    return wl


# Uses wordnet to create a dictionary of the words in the wordlist consisting of multiple definitions per word.
#   Saves the result as {language}_full_dictionary.json
def writeFullDictionary(language):
    wl = loadWordlist(language)
    full_dictionary = buildDictionary(wl, language)
    full_dictionary_filename = cm.mkpath('dictionary', language, '_full_dictionary.json')

    # Line reduction trick does not work for this one, use some search & replace to fix up the formatting a bit:
    encoded = json.dumps(full_dictionary, indent=2)
    encoded = encoded.replace('    [\n      "', '    ["')
    encoded = encoded.replace('",\n      "', '", "')
    encoded = encoded.replace('"\n    ]', '"]')

    cm.writeFile(full_dictionary_filename, encoded)
    print('Wrote %s' % full_dictionary_filename)


# Writes a reduced dictionary consisting of only one definition per word
#   If there is a dictionary of picked definitions available with a name of the form {language}_picked_definitions.json
#   use the definition in this dictionary, otherwise use the first definition in the {language}_all.json dictionary
#   Saves the result under {language}.json
def writeReducedDictionary(language):
    full_dictionary_filename = cm.mkpath('dictionary', language, '_full_dictionary.json')
    picked_definitions_filename = cm.mkpath('dictionary', language, '_picked_definitions.json')
    reduced_dictionary_filename = cm.mkpath('dictionary', language, '.json')

    full_dictionary = cm.loadJson(full_dictionary_filename)
    picked = cm.loadJson(picked_definitions_filename)
    wl = loadWordlist(language)
    reduced = {}
    for word in wl:
        # If a definition exists among the picked definitions, use that
        if word in picked:
            reduced[word] = picked[word]
        # Otherwise take the first word of the dictionary
        else:
            if word in full_dictionary and len(full_dictionary[word]) > 0:
                reduced[word] = full_dictionary[word][0]
            else:
                reduced[word] = ''
    cm.saveJson(reduced, reduced_dictionary_filename, compatArrays=True)


def main(language):
    if language == 'all':
        wordListPath = Path(PurePath(__file__).parent / 'wordlist')
        for wordlist_file in wordListPath.iterdir():
            if wordlist_file.is_file() and not wordlist_file.name.startswith('.'):
                print(language)
                language = wordlist_file.stem
                writeFullDictionary(language)
                writeReducedDictionary(language)
    else:
        print(language)
        writeFullDictionary(language)
        writeReducedDictionary(language)
    print('Wrote overview(s)')


main(used_language)
