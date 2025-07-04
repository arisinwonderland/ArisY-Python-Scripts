# Created 2025-07-03
# A script to process community-made .txt files containing data on cards for the now-defunct Weiss Schwarz Simulator.
# Weiss Schwarz is a Japanese CCG whose primary conceit is featuring cards of characters taken across numerous different franchises, thereby bringing in players from across various fandom spaces.
# The script outputs a .csv file containing the file name (in the first column) and corresponding card set identifier (in the second column) of each file passed to it.
# In the remaining columns, it produces a list of all "traits" included in each card set. Each "trait" describes a feature of the character represented by that card. Duplicates are stripped.
# I tested the script on 364 files provided by my client from across the internet. The script assumes one card set per .txt file.

import os
import re
        
INPUT_PATH = "data" # Point at a folder containing all files to be processed.
OUTPUT_PATH = "traits.csv"

files = os.listdir(INPUT_PATH)

sets = {} # Dict with filename as key and an tuple (identifier, set of traits) as value. If there were more card sets per file, I'd index on both filename and identifier, but this better reflected client's needs.

for file in files:
    if file.endswith(".txt"):
        file_path = os.path.join(INPUT_PATH, file)

        with open(file_path, "r", encoding="utf-8-sig") as f: # While not all test files were in UTF-8, this produced the best results. I thought about trying encoding detection, but decided that'd be overkill.
            try:
                l = ""
                for i in range(0,10): # Formatting for these files can be inconsistent; many have have commented-out preamble or extra newlines. Ten lines seems a little excessive, but five wasn't enough.
                    l = f.readline()
                    m = re.match(r"Character:? (\w+\/\w+)-", l) # Regex matching card set identifiers. There's a lot of variation, but matching the "Character" prefix and the hyphen seems to work well.
                    if m:
                        break

                if m:
                    set_name = m.group(1)
                    sets[file] = (set_name, set())
                    
                    for line in f:
                        m = re.match(r"Trait\d (.+)", line) # Regex matching lines with the "Trait" prefix. Cards can have up to three traits, so no quantifier for more digits is needed.
                        if m:
                            val = m.group(1).strip().replace('"','""') # None of the test data I used had quotes in the trait names, but it's best to be sure.
                            if re.search(",", val): # For neatness's sake, I've only put quotations around traits that actually have commas.
                                val = '"' + val + '"'
                            sets[file][1].add(val)
                else: # Runs if regex finds no match. In the test data, this error only occurred for one file that, on further inspection, had no character card data in it to begin with.
                    print('Match failed for filename "%s"'%(file))
            except UnicodeDecodeError: # In the test data, this error occurred for three files that were in UTF-16 rather than UTF-8 or ASCII. I decided this was an acceptable margin of error.
                print('Decoding failed for filename "%s"'%(file))
                continue
            
with open(OUTPUT_PATH, mode="w") as file:
    for key, value in sets.items(): # If not for the usage of the set to easily deduplicate traits, I might have used the csv library or Pandas rather than do this manually.
        line = "{filename},{setname},{traits}\n".format(filename=key, setname=value[0], traits=",".join(value[1]))
        file.write(line)
