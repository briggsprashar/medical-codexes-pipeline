# IMPORT necessary libraries
import pandas as pd 

import gc as gc
gc.collect() # force garbage collection to free up memory

import logging 
log = logging.getLogger(__name__) # logging setup

from datetime import datetime

# IMPORT shared function from utility folder to save transformed file to csv
from scripts.common_functions import save_to_csv

# LOAD hcpc dataset file from input\hcpcs folder (file has column heads))
hcpc_df = pd.read_excel (r'..\input\hcpcs\HCPC2025_OCT_ANWEB_v3.xlsx') 

# DISPLAY basic structure and column info
hcpc_df.info()

# PREVIEW first 5 rows
print(hcpc_df.head())

# EXPLORE key columns individually with column names for extraction
hcpc_df['HCPC']
hcpc_df['LONG DESCRIPTION']
hcpc_df['SHORT DESCRIPTION']

# CREATE a trimmed DataFrame with selected columns and assign it to a new VARIABLE
    # use of double square brackets to select multiple columns
    # use of copy() to create a copy of the selected columns
shorthcpc = hcpc_df[['HCPC', 'LONG DESCRIPTION']].copy()

# ADD a timestamp column for tracking updates with today's date in 'MM-DD-YYYY' format instead of a hardcoded timestamp
shorthcpc['last_updated'] = datetime.today().strftime('%m-%d-%Y')

# RENAME columns for clarity and consistency
shorthcpc = shorthcpc.rename(columns={'HCPC': 'Code', 'LONG DESCRIPTION': 'Description'})

# N/A: REMOVE empty descriptions/blanks/NaN values 

# N/A: REMOVE duplicate codes if any
    # shorthcpc = shorthcpc.drop_duplicates(subset=['HCPC'])

# SAVE this cleaned data subset as a CSV file using shared utility
save_to_csv(shorthcpc, 'hcpc_short.csv')

