import pandas as pd 
# import logging
# log = logging.getLogger(__name__)
from datetime import datetime
import sys
import gc

from rich.console import Console
console = Console()

import os 

folder_path = r"utils" 
if os.path.isdir(folder_path):
    console.print("\n[green]Utils folder exists and is recognized.[green]")
else:
    console.print("\n[red]Utils Folder not recognized or does not exist.[/red]")


# Add the parent directory of the current file to the system path
    # This code takes care of terminal error that utils is not a module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.common_functions import save_to_csv 

hcpc_df = pd.read_excel ('input\\hcpcs\\HCPC2025_OCT_ANWEB_v3.xlsx') 

hcpc_df.to_csv('output/csv/hcpc_raw.csv', sep=',', index=False, header=True) # to explore raw file data

# DONE candidate code-block for common functions script?
rows, cols = hcpc_df.shape
console.print("\nRows", rows)
console.print("Columns", cols)
console.print("\n[bold green]Basic Info[/bold green]\n")
hcpc_df.info()
console.print("\n[bold green]Raw File Preview[/bold green]\n")
print(hcpc_df.head())
console.print("\n[bold green]ILOC[/bold green]\n")
print(hcpc_df.iloc[0])

# EXPLORE key columns individually with column names for extraction
hcpc_df['HCPC']
hcpc_df['LONG DESCRIPTION']
hcpc_df['SHORT DESCRIPTION']

# CREATE a trimmed DataFrame with selected columns and assign it to a new VARIABLE
        # use of double square brackets to select multiple columns
        # use of copy() to create a copy of the selected columns
shorthcpc = hcpc_df[['HCPC', 'LONG DESCRIPTION']].copy()

# ADD a timestamp column
shorthcpc['Last_updated'] = datetime.today().strftime('%m-%d-%Y')

# RENAME columns for clarity and consistency
shorthcpc = shorthcpc.rename(columns={'HCPC': 'Code', 'LONG DESCRIPTION': 'Description'})

# SAVE this cleaned data subset as a CSV file using shared utility
# shorthcpc.to_csv(r"output\\csv\\hcpc_short.csv")

# candidate code-block for common functions script?
    # truncating columns
shorthcpc = shorthcpc.map(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output\\csv\\hcpc_aligned.csv", "w") as f:
    f.write(shorthcpc.to_string(index=False))

# DONE candidate code-block for common functions script?
console.print("\n[bold green]Extracted File Preview[/bold green]\n")
print(shorthcpc.head())
console.print("\n[bold green]Summary[/bold green]\n")    
console.print("[green]>>> Raw file was explored. Column headers were identified and extracted.[/green]")
console.print("[green]>>> HCPC column was renamed Code.[/green]")
console.print("[green]>>> Long Description column was renamed Description.[/green]") 
console.print("[green]>>> Last Updated column was added.[/green]")
console.print("[green]>>> Output file with 3 columns - Code, Description and Last_updated - was generated.[/green]")
save_to_csv(shorthcpc, 'hcpc_short.csv')
console.print("[green]>>> Final fixed-column-width .csv file was generated and saved in the output folder.[/green]\n")

hcpc_df = None
del hcpc_df
shorthcpc = None
del shorthcpc

gc.collect()
console.print("\n[bold white]Memory cleared. Processing complete.[/bold white]\n")
