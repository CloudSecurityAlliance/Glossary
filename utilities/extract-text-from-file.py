#!/usr/bin/env python3

# This script takes a file as argv, determines the type (docx/pdf) and then
# extracts all the words, removes any stop words and then counts the words and
# produces a CSV with the data and links to the glossary

# We may not have a file extension so determine filetype first
# pip install python-magic-bin
# https://github.com/ahupp/python-magic
import magic

# PDF support
# pip install pdfminer.six
# https://github.com/pdfminer/pdfminer.six
import pdfminer

# DOCX support
# pip install python-docx
# https://github.com/python-openxml/python-docx
import docx

# Read the stop list into a list
# Read the glossary list into a list
# Read the file, put the words into a dict if not in stop list, key is the word, count:value is the count, glossary:url is the glossary entry
# Check if word is in glossary, if so link to it
# Output results as CSV (filename-output.csv)
