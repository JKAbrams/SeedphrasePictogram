# SeedphrasePictogram
The Bitcoin Seedphrase Pictogram Project

## About
The goal is to have a set of freely available well suited pictograms for Bitcoin recovery seed phrases that can be used as a visual memory guide to more easily remember seed phrases.
In addition to the pictograms are dictionaries to complement the memorization by giving a deeper understanding of the words.

## Project guidelines
### What makes a good pictogram for this purpose?
* The picture is clearly distinguishable from any other picture in the set.
* There is a two-way recognition between the picture and the word, i.e. it is possible to unambiguously go from one word in the set to one picture in the set and conversely it is possible to go from one picture in the set to one word in the set.
* It has an unencumbered license or no license at all which makes it available for any purpose.

### Guiding rules for picking dictionary definitions
* One definition that finds the ground essence of the word in an inclusive way.
* Brevity rather than pedantry, without losing too much precision.
* A more tangible aspect is better than a less tangible aspect of the words meaning. Concreteness is beneficial as it leads to better integration between the pictograms and the words.
* Discourage circular definitions
* If a word have several meanings where a common essence is not what one thinks of, the most everyday recognizable meaning is used.
    For example: _drum_ can mean both a musical percussion instrument or basically anything that has a cylinder form, here the instrument is used.
* Synchronize the definitions and the pictograms

### Main sources for definitions
* Wordnet
* Wiktionary, Wiktionary simple English

## Status
6% of the English set has pictures.
There is an English dictionary, it contains for the project handpicked particularly fitting definitions for about half of the words.
The other languages are mostly stubs but many do contain automatically generated definitions, unfortunately the definitions are in English.

## Scripts and project organization
### Folder structure
* **dictionary** contains the dictionaries i .json format
The dictionaries are organized as follows:
  * `[language].json` - The main dictionary, one definition per word, uses the picked definitions where they are defined, uses the first definition from the full dictionary when not. Automatically generated.
  * `[language]_complementary.json` - Additional definitions not found in Wordnet.
  * `[language]_full.json` - All definitions contained in Wordnet + all complimentary definitions.
  * `[language]_picked_definitions.json` - Definitions picked from the full set, one definition per word. Automatically generated.

* **wordlist** contains the Bitcoin wordlists these are not expected to change but new languages might be added.
There is also the beginnings of a swedish wordlist, this is a WIP with about half of the required words.
* **pictograms** contains the pictograms

### Generator scripts
The scripts are Python 3 scripts, they require Python NLTK with the OWM-1.4 set.
* `tablemaker.py` Generates the Overview_[language].md files from the wordlists and the pictures available in the pictograms folder.
* `dictionary_maker.py` Generates the dictionaries [language].json and [language]_full.json Needs to be run before dictionary_table_maker.py
* `dictionary_table_maker.py` Generates the Dictionary_[language].md files from [language].json

## Word of caution
Please don't use this list to memorize important seed phrases until it reaches a level of stability.
The list is not yet complete and the pictures can change without notice.
