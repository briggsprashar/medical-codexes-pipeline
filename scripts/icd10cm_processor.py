import pandas as pd 
# import logging 
# log = logging.getLogger(__name__)
from datetime import datetime
import sys

from rich.console import Console
console = Console()

import os 
folder_path = "utils"
if os.path.isdir(folder_path):
     console.print("\n[green]Utils Folder exists and is recognized.[green]")
else:
    console.print("\n[red]Utils Folder not recognized or does not exist.[/red]")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.common_functions import save_to_csv

# LOAD icd-10 US dataset file with no headers as a fwf file
icd10us = pd.read_fwf(r'input\icd10US\icd10cm_order_2025.txt', header=None, 
# ASSIGN meaningful column names  
names=['Number', 'Code', 'Level', 'Description1', 'Description2'])

icd10us.to_csv('output\csv\icd10us_raw.csv', sep=',', index=False, header=True) # to explore raw file data

rows, cols = icd10us.shape
console.print("\nRows", rows)
console.print("Columns", cols)
console.print("\n[bold green]Basic Info[/bold green]\n")
icd10us.info()
console.print("\n[bold green]Preview 1st 5 rows[/bold green]\n")
print(icd10us.head())
console.print("\n[bold green]Level Count[/bold green]\n")
print(icd10us.Level.value_counts())
console.print("\n[bold green]ILOC[/bold green]\n")
print(icd10us.iloc[0])

icd10us['Number']
icd10us['Code']
icd10us['Level']
icd10us['Description1']

shorticd10us = icd10us[['Code', 'Description1']].copy()

shorticd10us['last_updated'] = datetime.today().strftime('%m-%d-%Y')

shorticd10us = shorticd10us.rename(columns={'Description1': 'Description'})

# REMOVE empty descriptions/blanks/NaN values 
shorticd10us = shorticd10us[
    shorticd10us['Description'].notna() & 
    (shorticd10us['Description'].str.strip() != '')
    ]

# REMOVE duplicates
shorticd10us = shorticd10us.drop_duplicates(subset=['Code'])

# truncating columns
pd.set_option("display.max_colwidth", 30)
with open("output\\csv\\icd10us_aligned.csv", "w") as f:
    f.write(shorticd10us.to_string(index=False))
    
console.print("\n[bold green]Extracted File Preview[/bold green]\n")
print(shorticd10us.head())

console.print("\n[bold green]Summary[/bold green]\n")    
console.print("[green]>>> Raw file was explored. Column headers were identified and extracted.[/green]")
console.print("[green]>>> Code column was extracted.[/green]")
console.print("[green]>>> Description1 column was renamed Description.[/green]") 
console.print("[green]>>> Last Updated column was added.[/green]")
console.print("[green]>>> Output file with 3 columns - Code, Description and Last_updated - was generated.[/green]")
save_to_csv(shorticd10us, 'icd10us_short.csv')
console.print("[green]>>> Final fixed-column-width .csv file was generated and saved in the output folder.[/green]\n")