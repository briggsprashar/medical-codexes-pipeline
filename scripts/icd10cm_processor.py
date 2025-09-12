# IMPORT necessary libraries
import pandas as pd 
import logging 
log = logging.getLogger(__name__)
from datetime import datetime

# IMPORT shared function from utility folder to save transformed file to csv
from utils.common_functions import save_to_csv

# LOAD icd-10 US dataset file with no headers as a fwf file
# ASSIGN meaningful column names  
icd10us = pd.read_fwf(r'C:\Users\briggs\Downloads\SBU\Summer 2025\Fall 2025\HHA507\medical-codex-pipeline\input\icd10US\icd10cm_order_2025.txt', header=None, 
names=['Number', 'Code', 'Level', 'Description1', 'Description2'])

# DISPLAY basic structure and column info
icd10us.info()

# PREVIEW first 5 rows
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