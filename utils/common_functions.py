# deliver a utility function that saves either a Polars (fast df library) or Pandas (standard df library)
# to a csv file in a specific directory 

# import necessary libraries: polars, pandas and garbage collection

import pandas as pd
import polars as pl
import gc as gc 

# trigger garbage collection to free up memory immediately
gc.collect() 

# import Path from the builtin pathlib module for file system paths in a clean objected oriented way.
from pathlib import Path

# create a directory path object pointing to the output/csv directory where all csv files will be saved 
CSV_PATH = Path("output/csv")

# define a function "save_to_csv" that takes a dataframe (either Polars or Pandas) and a csv filename for output

def save_to_csv(df, filename):
    
    ###Save a DataFrame (Polars or pandas) to CSV in the output/csv directory###
    filepath = CSV_PATH / filename

# if df is polaris df. yes, use the write_csv method to save it to the specified filepath. 
# if df is a pandas df, use the to_csv method to save it to the specified filepath.
# if df is neither, raise a TypeError indicating unsupported df type.

    if isinstance(df, pl.DataFrame):
        df.write_csv(str(filepath))
    elif isinstance(df, pd.DataFrame):
        df.to_csv(filepath, index=False)
    else:
        raise TypeError(f"Unsupported DataFrame type: {type(df)}")
