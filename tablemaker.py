#!/usr/bin/env python3

from pathlib import Path, PurePath

# Build the overview.md

# The language to build, use 'all' to build all language for which a wordlist exists
language = 'all'


def write_overview(wordlist_language):
    wordListFile = PurePath(__file__).parent / 'wordlist' / ('%s.txt' % wordlist_language)
    with open(wordListFile, 'r', encoding='utf-8') as f:
        wordlist = [w.strip() for w in f.readlines()]

    total_words = 2048
    has_images = 0

    # Heading
    title = '# Overview %s\n\n' % wordlist_language.title()

    # Table heading
    table_heading = '# Words\n\n'

    # Table
    table = '| Word        | Pictogram     | Properties  | License | Credit |\n'
    table += '| ----------- |:-------------:|:-----------:|:-------:|-------:|\n'

    for word in wordlist:
        pictogram = ''
        pictogram_filename = PurePath(__file__).parent / 'pictograms' / ('%s.svg' % word)
        if Path(pictogram_filename).is_file():
            pictogram = '<img src="%s">' % pictogram_filename
            has_images += 1
        table += '| %s | %s |  |  |  |\n' % (word, pictogram)

    # Statistics
    statistics = '## Statistics\n\n'
    statistics += '%i / %i has images\n\n' % (has_images, total_words)

    # Write file
    contents = title + statistics + table_heading + table
    overview_filename = 'Overview_%s.md' % wordlist_language.capitalize()
    with open(overview_filename, 'w') as f:
        f.write(contents)


def main():
    if language == 'all':
        wordListPath = Path(PurePath(__file__).parent / 'wordlist')
        for wordlist_file in wordListPath.iterdir():
            if wordlist_file.is_file() and not wordlist_file.name.startswith('.'):
                write_overview(wordlist_file.stem)
    else:
        write_overview(language)
    print('Wrote overview(s)')


main()
