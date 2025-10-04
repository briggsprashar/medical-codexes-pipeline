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

rxnorm.to_csv(r"output\csv\rxnorm_raw.csv") # to explore raw file data

rows, cols = rxnorm.shape
console.print("\nRows", rows)
console.print("Columns", cols)
console.print("\n[bold green]Basic Info[/bold green]\n")
rxnorm.info()
console.print("\n[bold green]Preview 1st 5 rows[/bold green]\n")
print(rxnorm.head())
# console.print("\n[bold green]Status Count[/bold green]\n")
# print(rxnorm.STATUS.value_counts())
console.print("\n[bold green]ILOC[/bold green]\n")
print(rxnorm.iloc[0])

rxnorm['rxaui']
rxnorm['aui'] 
rxnorm['str']

# CREATE a trimmed DataFrame with selected columns and assign it to a new VARIABLE
    # use of double square brackets to select multiple columns
    # use of copy() to create a copy of the selected columns
rxnorm_short = rxnorm[['rxaui', 'aui']].copy()

rxnorm_short = rxnorm_short.rename(columns={
        'rxaui': 'Code',
        'aui': 'Description',
        })

#removing empty descriptions or nulls or blanks 
rxnorm_short = rxnorm_short[
    rxnorm_short['Description'].notna() & 
    (rxnorm_short['Description'].str.strip() != "")]

rxnorm_short['Last_updated'] = datetime.today().strftime('%m-%d-%Y')

console.print("\n[bold green]Extracted File Preview[/bold green]\n")
print(rxnorm_short.head())

# truncating columns
rxnorm_short = rxnorm_short.map(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output\\csv\\rxnorm_aligned.csv", "w") as f:
    f.write(rxnorm_short.to_string(index=False))

console.print("\n[bold green]Summary[/bold green]\n")    
console.print("[green]>>> Raw file was explored. Column headers were identified and extracted.[/green]")
console.print("[green]>>> rzaui column was renamed Code.[/green]")
console.print("[green]>>> aui column was renamed Description.[/green]") 
console.print("[green]>>> Last Updated column was added.[/green]")
console.print("[green]>>> Output file with 3 columns - Code, Description and Last_updated - was generated.[/green]")
save_to_csv(rxnorm_short, 'rxnorm_short.csv') 
console.print("[green]>>> Final fixed-column-width .csv file was generated and saved in the output folder.[/green]\n")

rxnorm = None
del rxnorm
rxnorm_short = None
del rxnorm_short

gc.collect()
console.print("\n[bold white]Memory cleared. Processing complete.[/bold white]\n")