import polars as pl
import pandas as pd
import pyarrow as pa
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

# Adding the parent directory of the current file to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.common_functions import save_to_csv

# Define the file path
npi_file_path = (r"input\\npi\\npidata.csv")

df_polars = pl.read_csv(npi_file_path, n_rows=10000)

print(set(df_polars.dtypes))


rows, cols = df_polars.shape
print("Number of rows:", rows)
print("Number of columns:", cols)
print(df_polars.head())

polars_small = df_polars.select([
    'NPI', 
    'Provider Last Name (Legal Name)'
])

## add in a last_updated column
polars_small = polars_small.with_columns(
    pl.lit('2025-09-03').alias('last_updated')
)

## rename colummns: code, description, last_updated
_polars_small = polars_small.rename({
    'NPI': 'Code',
    'Provider Last Name (Legal Name)': 'Description',
    'last_updated': 'Last_updated'
})

# Convert Polars DataFrame to pandas DataFrame
pandas_small = polars_small.to_pandas()

save_to_csv(pandas_small, "npi_short.csv")

# truncating columns
pandas_small = pandas_small.applymap(lambda x: str(x)[:27] + "..." if len(str(x)) > 50 else str(x))
with open("output/csv/npi_aligned.csv", "w") as f:
    f.write(pandas_small.to_string())