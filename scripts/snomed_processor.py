import pandas as pd
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

# Import shared utility for saving DataFrames to CSV
from utils.common_functions import save_to_csv

filepath = "input\\snomed\\snomed.txt"

# Load SNOMED CT description file (tab-delimited, limited to 100,000 rows for testing)
snomed = pd.read_csv(
    filepath,
    sep='\t',
    nrows=100000
)

snomed.to_csv(r"output\csv\snomed_raw.csv")

rows, cols = snomed.shape
print("Number of rows:", rows)
print("Number of columns:", cols)
snomed.info()
print(snomed.head())

# Explore key columns
snomed['id']
snomed['term']
snomed['caseSignificanceId']

# Create a simplified DataFrame with selected columns
shortsnomed = snomed[['id', 'term']].copy()

# Add timestamp column for tracking updates
shortsnomed['Last_updated'] = datetime.today().strftime('%m-%d-%Y')

# Rename columns for clarity and consistency
shortsnomed = shortsnomed.rename(columns={
    'id': 'Code',
    'term': 'Description'
})

# Remove duplicate rows
shortsnomed = shortsnomed.drop_duplicates()

# Filter out empty or null descriptions
shortsnomed = shortsnomed[
    shortsnomed['Description'].notna() &
    (shortsnomed['Description'].str.strip() != "")
]

# Save cleaned subset to CSV using shared utility
save_to_csv(shortsnomed, 'snomed_short.csv')

# truncating columns
shortsnomed = shortsnomed.applymap(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output\csv\snomed_aligned.csv", "w") as f:
    f.write(shortsnomed.to_string(index=False))
