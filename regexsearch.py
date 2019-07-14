#! python3

# Open all .txt files in a folder
# Searches for any line that:
#   - matches usr supplied regex
# Print results to screen

import os, re

inp_text = input("Please input a regex you want to search for: ")
regex = re.compile(r'.*{}.*'.format(inp_text), re.IGNORECASE)

path = './regexsearchtest'

for filenames in os.listdir(path):
    with open(os.path.join(path, filenames)) as myfile:
        content = myfile.read()
        found = regex.findall(content,)
        if found != []:
            print(str(found) + ' in: {}'.format(filenames))