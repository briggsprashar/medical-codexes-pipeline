import polars as pl
import pandas as pd
import gc as gc 

gc.collect()

from pathlib import Path

CSV_PATH = Path("\output\csv")

def save_to_csv(df, filename):
    ###Save a DataFrame (Polars or pandas) to CSV in the output/csv directory###
    filepath = CSV_PATH / filename

    if isinstance(df, pl.DataFrame):
        df.write_csv(str(filepath))
    elif isinstance(df, pd.DataFrame):
        df.to_csv(filepath, index=False)
    else:
        raise TypeError(f"Unsupported DataFrame type: {type(df)}")