import pandas as pd
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

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.common_functions import save_to_csv

# Load SNOMED CT description file (tab-delimited, limited to 100,000 rows for testing)
filepath = "input\\snomed\\snomed.txt"
snomed = pd.read_csv(
    filepath,
    sep='\t',
    nrows=100000
    )

snomed.to_csv(r"output\csv\snomed_raw.csv") # to explore raw file data

rows, cols = snomed.shape
console.print("\nRows", rows)
console.print("Columns", cols)
console.print("\n[bold green]Basic Info[/bold green]\n")
snomed.info()
console.print("\n[bold green]Preview 1st 5 rows[/bold green]\n")
print(snomed.head())
console.print("\n[bold green]term Count[/bold green]\n")
print(snomed.term.value_counts())
console.print("\n[bold green]caseSignificanceId Count[/bold green]\n")
print(snomed.caseSignificanceId.value_counts())
console.print("\n[bold green]ILOC[/bold green]\n")
print(snomed.iloc[0])

# Explore key columns
snomed['id']
snomed['term']
snomed['caseSignificanceId']

# Create a simplified DataFrame with selected columns
shortsnomed = snomed[['id', 'term']].copy()

shortsnomed['Last_updated'] = datetime.today().strftime('%m-%d-%Y')

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

console.print("\n[bold green]Extracted File Preview[/bold green]\n")
print(shortsnomed.head())

# truncating columns
shortsnomed = shortsnomed.map(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output\\csv\\snomed_aligned.csv", "w") as f:
    f.write(shortsnomed.to_string(index=False))

console.print("\n[bold green]Summary[/bold green]\n")    
console.print("[green]>>> Raw file was explored. Column headers were identified and extracted.[/green]")
console.print("[green]>>> id column was renamed Code.[/green]")
console.print("[green]>>> term column was renamed Description.[/green]") 
console.print("[green]>>> Last Updated column was added.[/green]")
console.print("[green]>>> Output file with 3 columns - Code, Description and Last_updated - was generated.[/green]")
save_to_csv(shortsnomed, 'snomed_short.csv')
console.print("[green]>>> Final fixed-column-width .csv file was generated and saved in the output folder.[/green]\n")

snomed = None
del snomed
shortsnomed = None
del shortsnomed

gc.collect

console.print("\n[bold white]Memory cleared. Processing complete.[/bold white]\n")
