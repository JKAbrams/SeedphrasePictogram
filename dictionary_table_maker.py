#!/usr/bin/env python3
from pathlib import Path, PurePath
from nltk.corpus import wordnet as wn
import os
import common as cm

used_language = 'all'


# Analyze word classes, takes a list of words, returns a list of word classes:
def printWordClasses(wordlist):
    for word in wordlist:
        line = word + ', '
        for cls in wn.synsets(word):
            line += cls.pos()
        print(line)


# Build json
def buildJsonDictionary(wordlist, language):
    dictionary = {}
    filename = "%s/%s_complementary.json" % (os.path.join(os.path.dirname(__file__), "dictionary"), language)
    complimentary = cm.loadJson(filename)
    for word in wordlist:
        arr = []

        # loop through wn for this word
        for cls in wn.synsets(word):
            arr.append([cls.pos(), cls.definition()])

        # if it did not exist, look in the complimentary dictionary
        if not arr:
            if word in complimentary:
                arr = complimentary[word]

        dictionary[word] = arr
    return dictionary


# Analyze word classes, takes a list of words, returns a list of word classes:
def getWordClasses(wordlist):
    print('Loading dictionaries...')
    adjectives = {x.name().split('.', 1)[0] for x in wn.all_synsets('a')}
    print('* %i adjectives loaded' % (len(adjectives)))
    nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
    print('* %i nouns loaded' % (len(nouns)))
    verbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('v')}
    print('* %i verbs loaded' % (len(verbs)))

    classes = []
    for word in wordlist:
        wordClass = ''
        if word in nouns:
            wordClass += 'Noun'
        if word in verbs:
            if not wordClass == '':
                wordClass += ', '
            wordClass += 'Verb'
        if word in adjectives:
            if not wordClass == '':
                wordClass += ', '
            wordClass += 'Adjectiv'
        if wordClass == '':
            wordClass = 'Unknown'
        classes.append(wordClass)
        print(wordClass)

    return classes


def buildMarkdown(language):
    markdown = ''
    markdown += '# %s dictionary\n\n' % language
    markdown += '| Word | Class | Definition |\n'
    markdown += '| ---- |:-----:|:---------- |\n'

    dictionary_filename = cm.mkpath('dictionary', language, '.json')
    wordlist_filename = cm.mkpath('wordlist', language, '.txt')

    d = cm.loadJson(dictionary_filename)

    with open(wordlist_filename, "r", encoding="utf-8") as f:
        wl = [w.strip() for w in f.readlines()]

    last_word = ''
    for word in wl:
        word_on_line = word
        if word == last_word:
            word_on_line = ''
        last_word = word

        word_class = ''
        definition = ''
        if word in d and len(d[word]) > 1:
            word_class_short = d[word][0]
            word_class = cm.word_classes[word_class_short]
            definition = d[word][1]

        markdown += '| %s | %s | %s |\n' % (word_on_line, word_class, definition)

    markdown += '\n'
    return markdown


def main(language):
    if language == 'all':
        wordListPath = Path(PurePath(__file__).parent / 'wordlist')
        for wordlist_file in wordListPath.iterdir():
            if wordlist_file.is_file() and not wordlist_file.name.startswith('.'):
                language = wordlist_file.stem
                print(language)
                md = buildMarkdown(language)
                filename = cm.mkpath('', 'Dictionary_%s' % language, '.md')
                cm.writeFile(filename, md)
    else:
        print(language)
        md = buildMarkdown(language)
        filename = cm.mkpath('', 'Dictionary_%s' % language, '.md')
        cm.writeFile(filename, md)
    print('Wrote overview(s)')


main(used_language)
