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
   console.print("\n[green]Utils Folder exists and is recognized.[/green]")
else:
    console.print("\n[red]Utils Folder not recognized or does not exist.[/red]")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.common_functions import save_to_csv

# LOAD icd-10 WHO dataset file with no headers
# ASSIGN column names
icd10who = pd.read_csv(r'input\icd10WHO\icd102019syst_codes.txt', header=None, sep=';',
    names = ['Level', 'Type', 'Usage', 'Sort', 'Parent', 'Code', 'Display_code', 'Icd10_code', 
        'Title_en', 'Parent_title', 'Detailed_title', 'Definition', 'Mortality_code',
        'Morbidity_code1', 'Morbidity_code2', 'Morbidity_code3', 'Morbidity_code4',     
        ])

icd10who.to_csv('output/csv/icd10who_raw.csv', sep=',', index=False, header=True) # to explore raw file data

rows, cols = icd10who.shape
console.print("\nRows", rows)
console.print("Columns", cols)
console.print("\n[bold green]Basic Info[/bold green]\n")
icd10who.info()
console.print("\n[bold green]Preview 1st 5 rows[/bold green]\n")
print(icd10who.head())
console.print("\n[bold green]Type Count[/bold green]\n")
print(icd10who.Type.value_counts())
console.print("\n[bold green]Usage Count[/bold green]\n")
print(icd10who.Usage.value_counts())
console.print("\n[bold green]ILOC[/bold green]\n")
print(icd10who.iloc[0])

icd10who['Display_code']    
icd10who['Detailed_title']
icd10who['Icd10_code']

shorticd10who = icd10who[['Display_code', 'Detailed_title']].copy()

# REMOVE empty descriptions/blanks/NaN values 
shorticd10who = shorticd10who[
    shorticd10who['Detailed_title'].notna() & 
    (shorticd10who['Detailed_title'].str.strip() != '')
    ]

shorticd10who = shorticd10who.rename(columns={
    'Display_code': 'Code',
    'Detailed_title': 'Description'
    })

shorticd10who['Last_updated'] = datetime.today().strftime('%m-%d-%Y')


# REMOVE duplicate codes if any
#shorticd10who = shorticd10who.drop_duplicates(subset=['Icd10_code'])

# truncating columns
shorticd10who = shorticd10who.map(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output\\csv\\icd10who_aligned.csv", "w") as f:
    f.write(shorticd10who.to_string(index=False))

console.print("\n[bold green]Extracted File Preview[/bold green]\n")
print(shorticd10who.head())

console.print("\n[bold green]Summary[/bold green]\n")    
console.print("[green]>>> Raw file was explored. Column headers were identified and extracted.[/green]")
console.print("[green]>>> Code column was extracted.[/green]")
console.print("[green]>>> Description1 column was renamed Description.[/green]") 
console.print("[green]>>> Last Updated column was added.[/green]")
console.print("[green]>>> Output file with 3 columns - Code, Description and Last_updated - was generated.[/green]")
save_to_csv(shorticd10who, 'icd10who_short.csv') 
console.print("[green]>>> Final fixed-column-width .csv file was generated and saved in the output folder.[/green]\n")
