# import pandas package
import pandas as pd 
import logging
log = logging.getLogger(__name__)
from datetime import datetime

# 
filepath = 'input/LOINC/Loinc.csv'

df = pd.read_csv(filepath)
print(df.head())
df.to_csv('output/csv/loinc_test.csv')

# read csv data from identified file into a pandas dataframe named loinc to query and 
# process the data efficiently
loinc = pd.read_csv(r'C:\Users\briggs\Downloads\SBU\Summer 2025\Fall 2025\HHA507\medical-codex-pipeline\input\loinc\Loinc.csv')

# print column names, number of columns, data types, and how much memory the dataframe uses.
# quick structure overview 
loinc.info()

# count frequency of unique values found in the status column
loinc.STATUS.value_counts()

# show all fields of the first row 
loinc.iloc[0]

loinc.LOINC_NUM 
loinc.LONG_COMMON_NAME
list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']

loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
loinc_small = loinc[list_cols]

loinc_small['last_updated'] = '2025-09-03'

# loinc_small = loinc_small.rename(columns={})

loinc_small = loinc_small.rename(columns={
        'LOINC_NUM': 'code',
        'LONG_COMMON_NAME': 'description',
        })

file_output_path = 'C:\Users\briggs\Downloads\SBU\Summer 2025\Fall 2025\HHA507\medical-codex-pipeline\output\csv\loinc_small.csv'
loinc_small.to_csv(r'C:\Users\briggs\Downloads\SBU\Summer 2025\Fall 2025\HHA507\medical-codex-pipeline\output\csv\loinc_small.csv')
loinc_small.to_csv(r'C:\Users\briggs\Downloads\SBU\Summer 2025\Fall 2025\HHA507\medical-codex-pipeline\output\csv\loinc_small_noindex.csv', index=False)
