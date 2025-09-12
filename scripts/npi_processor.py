# IMPORT necessary libraries
import pandas as pd 
import polars as pl

import gc as gc
gc.collect() # force garbage collection to free up memory

import logging 
log = logging.getLogger(__name__) # logging setup

from datetime import datetime

# IMPORT shared function from utility folder to save transformed file to csv
from utils.common_functions import save_to_csv

# IDENTIFY path for dataset file
npi_file_path = '..\input\npidata.csv'

# LOAD npi dataset file using polars (first 1000 rows only)
start_time_polars = time.time()
df_polars = pl.read_csv(npi_file_path, n_rows=1000)

# (A random sample code in comment below with a fixed seed for reproducibility was also tested but not used here)
# random_sample = df.sample(n=1000, seed=42)

# Code for time elapsed was ignored

# DISPLAY basic dataset info
print(f"Loaded {len(npicode)} records") # prints row numbers
print(f"Columns: {npicode.columns}") # prints column header names
print(f"Shape: {npicode.shape}") # prints shape (rows, columns) (tuple)
print("\n Preview:") # prints a new line and 'Preview' as a label

# PREVIEW first 5 rows
print(npicode.head()) 

# SELECT relevant columns for extraction
print(f"Successfully loaded {len(df_polars)} records from NPI data")
print(f"Columns: {df_polars.columns}")
print(f"\nDataset shape: {df_polars.shape}")
print(f"\nFirst 5 rows:")
print(df_polars.head())

# MEMORY usage details. (ideally time-elapsed (ignored above) and memory-used should be in a single function that can be called)
print(f"\n Memory usage (MB): {df.estimated_size() / 1024**2:.2f}")


df_polars_small = df_polars.select([
    'NPI', 
    'Provider Last Name (Legal Name)'
])

## add in a last_updated column
df_polars_small = df_polars_small.with_columns(
    pl.lit('2025-09-03').alias('last_updated')
)

## rename colummns: code, description, last_updated
df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
    'last_updated': 'last_updated'
})


## save to csv
output_path = 'Module1_MedicalCodexes/npi/output/npi_small.csv'
df_polars_small.write_csv(output_path)
df_polars_small.write_parquet('Module1_MedicalCodexes/npi/output/npi_small.parquet')









