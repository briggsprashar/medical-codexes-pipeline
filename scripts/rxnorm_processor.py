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

# LOAD RxNorm dataset file with no headers as a pipe-delimited file

filepath = "input\\rxnorm\\RXNATOMARCHIVE.RRF"

columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]
# Load the data into a pandas DataFrame
rxnorm = pd.read_csv(
    filepath,
    sep='|',
    header=None,
    names=columns,
    on_bad_lines='warn'
    )

rxnorm.to_csv(r"output\csv\rxnorm_raw.csv")


rows, cols = rxnorm.shape
print("Number of rows:", rows)
print("Number of columns:", cols)
rxnorm.info()
print(rxnorm.head())

rxnorm['rxaui']
rxnorm['aui'] 
rxnorm['str']

# CREATE a trimmed DataFrame with selected columns and assign it to a new VARIABLE
    # use of double square brackets to select multiple columns
    # use of copy() to create a copy of the selected columns
rxnorm_short = rxnorm[['rxaui', 'aui']].copy()

rxnorm_short['Last_updated'] = datetime.today().strftime('%m-%d-%Y')

rxnorm_short = rxnorm_short.rename(columns={
        'rxaui': 'Code',
        'aui': 'Description',
        })


#removing empty descriptions or nulls or blanks 
rxnorm_short = rxnorm_short[
    rxnorm_short['Description'].notna() & 
    (rxnorm_short['Description'].str.strip() != "")]

save_to_csv(rxnorm_short, 'rxnorm_short.csv') 

# truncating columns
rxnorm_short = rxnorm_short.applymap(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output\\csv\\rxnorm_aligned.csv", "w") as f:
    f.write(rxnorm_short.to_string(index=False))