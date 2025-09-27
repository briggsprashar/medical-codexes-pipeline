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

# LOAD icd-10 US dataset file with no headers as a fwf file
# ASSIGN meaningful column names  
icd10us = pd.read_fwf(r'input\icd10US\icd10cm_order_2025.txt', header=None, 
names=['Number', 'Code', 'Level', 'Description1', 'Description2'])

rows, cols = icd10us.shape
print("Number of rows:", rows)
print("Number of columns:", cols)
icd10us.info()
print(icd10us.head())

# EXPLORE key columns individually with column names (named above) for extraction
icd10us['Number']
icd10us['Code']
icd10us['Level']
icd10us['Description1']

# CREATE a trimmed DataFrame with selected columns and assign it to a new VARIABLE
    # use of double square brackets to select multiple columns
    # use of copy() to create a copy of the selected columns
shorticd10us = icd10us[['Code', 'Description1']].copy()

# ADD a timestamp column for tracking updates with today's date in 'MM-DD-YYYY' format instead of a hardcoded timestamp
shorticd10us['last_updated'] = datetime.today().strftime('%m-%d-%Y')

# RENAME columns for clarity and consistency
shorticd10us = shorticd10us.rename(columns={'Description1': 'Description'})

# REMOVE empty descriptions/blanks/NaN values 
shorticd10us = shorticd10us[
    shorticd10us['Description'].notna() & 
    (shorticd10us['Description'].str.strip() != '')
    ]

# REMOVE duplicate codes if any
shorticd10us = shorticd10us.drop_duplicates(subset=['Code'])

# SAVE this cleaned data subset as a CSV file using shared utility
save_to_csv(shorticd10us, 'icd10us_short.csv')

# truncating columns
# the code snipper below aligns the output file to fixed column width
pd.set_option("display.max_colwidth", 30)
with open("output\csv\icd10us_aligned.csv", "w") as f:
    f.write(shorticd10us.to_string(index=False))

    