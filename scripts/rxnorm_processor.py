# IMPORT necessary libraries
import pandas as pd 

import gc as gc
gc.collect() # force garbage collection to free up memory

import logging 
log = logging.getLogger(__name__) # logging setup

from datetime import datetime

# IMPORT shared function from utility folder to save to save transformed file to csv
from utils.common_functions import save_to_csv

# LOAD RxNorm dataset file with no headers as a pipe-delimited file
rxnorm = pd.read_csv(r'C:\Users\briggs\Downloads\SBU\Summer 2025\Fall 2025\HHA507\medical-codex-pipeline\input\rxnorm\RXNATOMARCHIVE.RRF', 
        header=None, delimiter='|', dtype=str)

# DISPLAY basic structure and column info
rxnorm.info()

# PREVIEW first 5 rows
print(rxnorm.head())

# EXPLORE key columns individually by index for extraction
rxnorm[1], rxnorm[2], rxnorm[3]

# CREATE a trimmed DataFrame with selected columns and assign it to a new VARIABLE
    # use of double square brackets to select multiple columns
    # use of copy() to create a copy of the selected columns
rxnorm_short = rxnorm[[1, 2, 3]].copy()

# ADD a timestamp column for tracking updates with today's date in 'MM-DD-YYYY' format instead of a hardcoded timestamp
rxnorm_short['last_updated'] = datetime.today().strftime('%m-%d-%Y')

# N/A: RENAME columns for clarity and consistency

