# IMPORT necessary libraries
import pandas as pd 
import logging
log = logging.getLogger(__name__)
from datetime import datetime

# IMPORT shared function from utility folder to save to save transformed file to csv
from utils.common_functions import save_to_csv

# LOAD icd-10 WHO dataset file with no headers
# ASSIGN column names
icd10who = pd.read_csv(r'C:\Users\briggs\Downloads\SBU\Summer 2025\Fall 2025\HHA507\medical-codex-pipeline\input\icd10WHO\icd102019syst_codes.txt', header=None, sep=';',
    names = ['Level', 'Type', 'Usage', 'Sort', 'Parent', 'Code', 'Display_code', 'Icd10_code', 
        'Title_en', 'Parent_title', 'Detailed_title', 'Definition', 'Mortality_code',
        'Morbidity_code1', 'Morbidity_code2', 'Morbidity_code3', 'Morbidity_code4',     
        ])

# Columns can also be named with the following code
    # columns = ['Level', etc]
    # df = pd.read_csv(file_path, sep=';', header=None, names=columns)

# DISPLAY basic structure and column info
icd10who.info()

# PREVIEW first 5 rows
print(icd10who.head())

# EXPLORE key columns individually with column names (named above) for extraction
icd10who['Display_code']    
icd10who['Detailed_title']
icd10who['Icd10_code']

'''
# NAME columns individually with column names for extraction
# icd10who = icd10who.rename(columns={
    0: 'Level', 
    1: 'Type', 
    2: 'Usage', 
    3: 'Sort', 
    4: 'Parent', 
    5: 'Code', 
    6: 'Display_code',
    7: 'Icd10_code', 
    8: 'Title_en', 
    9: 'Parent_title', 
    10: 'Detailed_title', 
    11: 'Definition', 
    12: 'Mortality_code', 
    13: 'Morbidity_code1', 
    14: 'Morbidity_code2',
    15: 'Morbidity_code3', 
    16: 'Morbidity_code4',          
    }) 
'''

# CREATE a trimmed DataFrame with selected columns and assign it to a new VARIABLE
    # use of double square brackets to select multiple columns
    # use of copy() to create a copy of the selected columns
shorticd10who = icd10who[['Display_code', 'Detailed_title']].copy()

# ADD a timestamp column for tracking updates with today's date in 'MM-DD-YYYY' format instead of a hardcoded timestamp
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