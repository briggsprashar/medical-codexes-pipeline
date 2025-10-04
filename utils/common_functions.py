import pandas as pd
import polars as pl
from pathlib import Path
import gc
from rich.console import Console
console = Console()

# define a function "save_to_csv" that takes a dataframe (either Polars or Pandas) and a csv filename for output\
def save_to_csv(df, filename):
    output_dir = Path("output\\csv")
    output_dir.mkdir(parents=True, exist_ok=True)

    filepath = output_dir / filename # Save a DataFrame (Polars or pandas) to CSV in the output/csv directory

    if isinstance(df, pl.DataFrame):
        df.write_csv(str(filepath)) # if df is polaris df, use the write_csv method to save it to the specified filepath. 
    elif isinstance(df, pd.DataFrame):
        df.to_csv(filepath, index=False) # if df is a pandas df,use the to_csv method to save it to the specified filepath.
    else:
        raise TypeError(f"Unsupported DataFrame type: {type(df)}") # if df is neither, raise a TypeError indicating unsupported df type.
    console.print("[bold green]Processed data with 3 columns extracted to[/bold green]", filepath)
    
    gc.collect()