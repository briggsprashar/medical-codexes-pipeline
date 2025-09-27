import pandas as pd 
# import logging
# log = logging.getLogger(__name__)
from datetime import datetime
import sys

import os 
folder_path = "utils"
if os.path.isdir(folder_path):
    print("Folder exists and is recognized.")
else:
    print("Folder not recognized or does not exist.")

# Add the parent directory of the current file to the system path
# This code takes care of terminal error that utils is not a module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.common_functions import save_to_csv

# LOAD icd-10 WHO dataset file with no headers
# ASSIGN column names
icd10who = pd.read_csv(r'input\icd10WHO\icd102019syst_codes.txt', header=None, sep=';',
    names = ['Level', 'Type', 'Usage', 'Sort', 'Parent', 'Code', 'Display_code', 'Icd10_code', 
        'Title_en', 'Parent_title', 'Detailed_title', 'Definition', 'Mortality_code',
        'Morbidity_code1', 'Morbidity_code2', 'Morbidity_code3', 'Morbidity_code4',     
        ])

rows, cols = icd10who.shape
print("Number of rows:", rows)
print("Number of columns:", cols)
icd10who.info()
print(icd10who.head())

save_to_csv(icd10who, 'icd10who_raw.csv') 

# EXPLORE key columns individually with column names (named above) for extraction
icd10who['Display_code']    
icd10who['Detailed_title']
icd10who['Icd10_code']

# CREATE a trimmed DataFrame with selected columns and assign it to a new VARIABLE
    # use of double square brackets to select multiple columns
    # use of copy() to create a copy of the selected columns
shorticd10who = icd10who[['Display_code', 'Detailed_title']].copy()

#### rename detailed_title to Description ####

shorticd10who['last_updated'] = datetime.today().strftime('%m-%d-%Y')

# REMOVE empty descriptions/blanks/NaN values 
shorticd10who = shorticd10who[
    shorticd10who['Detailed_title'].notna() & 
    (shorticd10who['Detailed_title'].str.strip() != '')
    ]

# REMOVE duplicate codes if any
#shorticd10who = shorticd10who.drop_duplicates(subset=['Icd10_code'])

# SAVE this cleaned data subset as a CSV file using shared utility
save_to_csv(shorticd10who, 'icd10who_short.csv') 

# the code snipper below aligns the output file to fixed column width
# pd.set_option("display.max_colwidth", 10)
# with open("output\csv\icd10who_aligned.csv", "w") as f:
#  f.write(shorticd10who.to_string(index=False))

# truncate column widths in output files    
# pd.set_option("display.max_colwidth", 30)
# with open("output\csv\icd10who_aligned.csv", "w") as f:
#    f.write(shorticd10who.to_string(index=False))

# truncating columns
shorticd10who = shorticd10who.applymap(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output\csv\icd10who_aligned.csv", "w") as f:
    f.write(shorticd10who.to_string(index=False))

    