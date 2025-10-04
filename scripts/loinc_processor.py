import pandas as pd 
# import logging
# log = logging.getLogger(__name__)
from datetime import datetime
import sys
import gc

from rich.console import Console
console = Console()

import os 
folder_path = "utils"
if os.path.isdir(folder_path):
     console.print("\n[green]Utils Folder exists and is recognized.[/green]")
else:
    console.print("\n[red]Utils Folder not recognized or does not exist.[/red]")

# Add the parent directory of the current file to the system path
# This code takes care of terminal error that utils is not a module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.common_functions import save_to_csv

filepath = 'input\\loinc\\Loinc.csv'

loinc = pd.read_csv(filepath, low_memory=False)
loinc.to_csv('output\\csv\\loinc_raw.csv') # to explore raw file data

rows, cols = loinc.shape
console.print("\nRows", rows)
console.print("Columns", cols)
console.print("\n[bold green]Basic Info[/bold green]\n")
loinc.info()
console.print("\n[bold green]Preview 1st 5 rows[/bold green]\n")
print(loinc.head())
console.print("\n[bold green]Status Count[/bold green]\n")
print(loinc.STATUS.value_counts())
console.print("\n[bold green]ILOC[/bold green]\n")
print(loinc.iloc[0])

# Explore columns using list
loinc.LOINC_NUM 
loinc.LONG_COMMON_NAME

# create trimmed df with selected  columns 
list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME'].copy()

loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
loinc_small = loinc[list_cols]
loinc_small = loinc_small.rename(columns={
        'LOINC_NUM': 'Code',
        'LONG_COMMON_NAME': 'Description',
        })

loinc_small['Last_updated'] = datetime.today().strftime('%m-%d-%Y')

console.print("\n[bold green]Extracted File Preview[/bold green]\n")
print(loinc_small.head())

    # truncating columns
loinc_small = loinc_small.map(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output\\csv\\loinc_aligned.csv", "w") as f:
    f.write(loinc_small.to_string(index=False))

console.print("\n[bold green]Summary[/bold green]\n")    
console.print("[green]>>> Raw file was explored. Column headers were identified and extracted.[/green]")
console.print("[green]>>> LOINC_NUM column was extracted.[/green]")
console.print("[green]>>> LONG_COMMON_NAME column was renamed Description.[/green]") 
console.print("[green]>>> Last Updated column was added.[/green]")
console.print("[green]>>> Output file with 3 columns - Code, Description and Last_updated - was generated.[/green]")
save_to_csv(loinc_small, 'loinc_small.csv') 
console.print("[green]>>> Final fixed-column-width .csv file was generated and saved in the output folder.[/green]\n")

loinc = None
del loinc
loinc_small = None
del loinc_small

gc.collect()
console.print("\n[bold white]Memory cleared. Processing complete.[/bold white]\n")
