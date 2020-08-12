#!/bin/bash

cd ../diagrams/
#
# Get a list of all tags
#
allCategories=(`grep "^Category:" ../glossary/*/*.md | cut -d":" -f3 | sort | uniq`)


#printf '%s\n' "${allCategories[@]}"

for every_item in ${allCategories[@]}; do
    # Remove the line return from the array variable
    cleaned_every_item=${every_item/%$'\r'/}
    # Set a filename to dump to
    file_name="../diagrams/$cleaned_every_item.md"
    # Searchstring for the category tag
    search_string="^Category:$cleaned_every_item"
    #
    #
    # Create the file
    #
    echo "\`\`\`mermaid" > $file_name
    echo "graph TD" >> $file_name
    #
    # Apparently we can just put any root node in
    #
    echo "$cleaned_every_item($cleaned_every_item)" >> $file_name
    #
    # grep for the category tag, 20 lines before and after, then strip all the Graph tags out, and get the uniques ones, shove them into the file
    #
    grep -h -A20 -B20 $search_string ../glossary/*/*.md | grep "^Graph:" | sed 's/^Graph://' | sort | uniq  >> $file_name
    done
