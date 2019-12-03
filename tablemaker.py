#!/usr/bin/env python3

import sys
import os

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
    github_token = 'AAIP7CQZLPMDA773CNQYVTC542DNE'
    
    references = ''

    for word in wordlist:
        table += '| %s | ![%s][%s] |  |  |  |\n' % (word, word, word)

        references += '[%s]: %s%s.svg%s "%s"\n' % (word, github_url, word, github_token, word)

    # Write overview:
    contents = heading + table + references
    overview_filename = 'overview_%s.md' % (wordlist_language)
    with open(overview_filename, 'w') as f:    
        f.write(contents)
        
        
def main():
    if language == 'all':
        for wordlist_filename in os.listdir(cls._get_directory()):
            write_overview(wordlist_filename)
    else:
        write_overview(language)


main()