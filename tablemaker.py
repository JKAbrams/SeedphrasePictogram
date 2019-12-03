#!/usr/bin/env python3

import sys
import os
import os.path


# Build the overview.md

# The language to build, use 'all' to build all language for which a wordlist exists
language = 'english'


def write_overview(wordlist_language):
    with open("%s/%s.txt" % (os.path.join(os.path.dirname(__file__), "wordlist"), wordlist_language), "r", encoding="utf-8") as f:
        wordlist = [w.strip() for w in f.readlines()]
    
    # Add heading:
    heading = '# Overview English\n'

    heading += '| Word        | Pictogram     | Properties  | License | Credit |\n'
    heading += '| ----------- |:-------------:|:-----------:|:-------:|-------:|\n'

    table = ''

    github_url = 'https://raw.githubusercontent.com/JKAbrams/SeedphrasePictogram/master/pictograms/'
    
    references = ''

    for word in wordlist:
        pictogram_filename = '%s.svg' % (word)
        pictogram_reference = ''
        if os.path.isfile('pictograms/' + pictogram_filename):
            pictogram_reference = '![%s][%s]' % (word, word)
            references += '[%s]: "%s%s?sanitize=true"\n' % (word, github_url, pictogram_filename)
        table += '| %s | %s |  |  |  |\n' % (word, pictogram_reference)

    # Write overview:
    contents = heading + table + '\n' + references
    overview_filename = 'overview_%s.md' % (wordlist_language)
    with open(overview_filename, 'w') as f:    
        f.write(contents)
        
        
def main():
    if language == 'all':
        for wordlist_filename in os.listdir(cls._get_directory()):
            write_overview(wordlist_filename)
    else:
        write_overview(language)
    print('Wrote overview(s)')


main()