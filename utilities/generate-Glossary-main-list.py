\#!/usr/bin/python

# Generates the Glossary-main-list.txt in the local directory, assumes it is run from Glossary git repo root directory (./glossary/*/*.md basically)

import os

root_dir = "glossary"

fileoutput = "Glossary-main-list.txt"

with open(fileoutput, 'w') as results:
    for dir_, _, files in os.walk(root_dir):
        for file_name in files:
            results.write(file_name + "\n")
