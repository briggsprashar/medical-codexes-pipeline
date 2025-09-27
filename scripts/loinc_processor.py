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

filepath = 'input\loinc\Loinc.csv'

loinc = pd.read_csv(filepath, low_memory=False)
loinc.to_csv('output\\csv\\loinc_raw.csv') # to explore

rows, cols = loinc.shape
print("Number of rows:", rows)
print("Number of columns:", cols)
(loinc.info())
print(loinc.head())
(loinc.STATUS.value_counts())
(loinc.iloc[0])

# Explore columns using list
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

save_to_csv(loinc_small, 'loinc_small.csv') 

# the code snipper below aligns the output file to fixed column width
# pd.set_option("display.max_colwidth", 10)
# with open("output\csv\loinc_aligned.csv", "w") as f:
#    f.write(loinc_small.to_string(index=False))
    
# truncating columns
loinc_small = loinc_small.applymap(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output\csv\loinc_aligned.csv", "w") as f:
    f.write(loinc_small.to_string(index=False))
