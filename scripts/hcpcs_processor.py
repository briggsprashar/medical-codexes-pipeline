import pandas as pd 
# import logging
# log = logging.getLogger(__name__)
from datetime import datetime
import sys

import os 

folder_path = r"utils"
if os.path.isdir(folder_path):
    print("Folder exists and is recognized.")
else:
    print("Folder not recognized or does not exist.")

# Add the parent directory of the current file to the system path
# This code takes care of terminal error that utils is not a module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.common_functions import save_to_csv 

hcpc_df = pd.read_excel ('input\\hcpcs\\HCPC2025_OCT_ANWEB_v3.xlsx') 
# save_to_csv(hcpc_df, 'output\csv\hcpc_raw.csv')

rows, cols = hcpc_df.shape
print("Number of rows:", rows)
print("Number of columns:", cols)
hcpc_df.info()
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

# SAVE this cleaned data subset as a CSV file using shared utility
shorthcpc.to_csv(r"output\\csv\\hcpc_short.csv")

# truncating columns
shorthcpc = shorthcpc.applymap(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output\csv\hcpc_aligned.csv", "w") as f:
    f.write(shorthcpc.to_string(index=False))
    
    




