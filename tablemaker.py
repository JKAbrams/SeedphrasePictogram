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

    total_words = 2048
    has_images = 0
    
    # Heading
    title = '# Overview (%s)\n\n' % (wordlist_language)

    # Table heading
    table_heading = '# Words\n\n'

    # Table
    table  = '| Word        | Pictogram     | Properties  | License | Credit |\n'
    table += '| ----------- |:-------------:|:-----------:|:-------:|-------:|\n'
    
    for word in wordlist:
        pictogram = ''
        pictogram_filename = './pictograms/%s.svg' % (word)
        if os.path.isfile(pictogram_filename):
            pictogram = '<img src="%s">' % (pictogram_filename)
            has_images += 1
        table += '| %s | %s |  |  |  |\n' % (word, pictogram)

    # Statistics
    statistics = '## Statistics\n\n'
    statistics += '%i / %i has images\n\n' % (has_images, total_words)
    


    # Write file
    contents = title + statistics + table_heading + table
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