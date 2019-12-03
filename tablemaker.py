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
    
    for word in wordlist:
        pictogram = ''
        pictogram_filename = './pictograms/%s.svg' % (word)
        if os.path.isfile(pictogram_filename):
            pictogram = '<img src="%s">' % (pictogram_filename)
        table += '| %s | %s |  |  |  |\n' % (word, pictogram)

    # Write overview:
    contents = heading + table
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