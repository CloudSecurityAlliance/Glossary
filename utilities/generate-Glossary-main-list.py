#!/usr/bin/python3

# Generates the Glossary-main-list.txt in the local directory, assumes it is run from Glossary git repo root directory (./glossary/*/*.md basically)

import os
import re

root_dir = "glossary"

fileoutput = "glossary.txt"

with open(fileoutput, 'w') as results:
    for dir_, _, files in os.walk(root_dir):
        for file_name in files:
            file_name=re.sub(r"\.md$", "", file_name)
            results.write(file_name + "\n")
