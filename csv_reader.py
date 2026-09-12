"""CSV reading and processing utilities."""
import pandas as pd
from typing import Optional, List

def read_csv(filepath: str, encoding: str = 'utf-8') -> pd.DataFrame:
    return pd.read_csv(filepath, encoding=encoding)

def filter_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    return df[columns]

def summarize_csv(filepath: str) -> dict:
    df = read_csv(filepath)
    return {
        'rows': len(df),
        'columns': list(df.columns),
        'dtypes': df.dtypes.to_dict(),
        'missing': df.isnull().sum().to_dict()
    }
