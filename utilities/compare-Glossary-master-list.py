#!/usr/bin/python

# Compares the Glossary-master-list.txt in the local directory against ARGV0 (a text file) and does a fuzzy-wuzzy comparision and generates a report showing the highest match for each word in the new text file

import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

file_glossary = "Glossary-master-list.txt"

file_compare=sys.argv[1]

comparision_results={}

# For now we just do fuzzywuzzy compare and report highest score for each word in file_compare

with open(file_glossary) as filedata_glossary:
    lines_glossary = [line.rstrip('.md\n') for line in filedata_glossary]

with open(file_compare) as filedata_compare:
    lines_compare = [line.rstrip('\n') for line in filedata_compare]

for item_in_compare in lines_compare:
    comparision_results = process.extract(item_in_compare, lines_glossary)
    print(comparision_results)
# Now to decide how to present them to the user and what to do with them.
#
# How to handle:
# 1) exact matches (100) of primary file and long term of alias
# 2) really close matches (perentage? additional string compares? do a simple poor mans test as well?) of primary file and long term of alias
# 3) stuff with no match of primary file and long term of alias?
# 4) how to handle the stop list, we'll need to put that data in as well
#
# We'll generate a CSV output file with the file_compare entries and then:
# Any exact match with the stop list ("stoplist_match":"yes_stoplist"/"no_stoplist")?
# 1-5 closest matches with the stop list? (actual score and entry)
# Any exact match with the existing glossary primary term or alias ("exact_match":"yes_primary"/"yes_alias"/"no")?
# 1-5 closest matches with the primary terms (actual score and entry?)
# 1-5 closest matchees with the aliases (actual score and entry?)
#
# TODO: once we have aliases, we'll need the generate-Glossary-master-list.py to also generate a list of aliases in a file
