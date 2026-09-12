"""Data cleaning and preprocessing utilities."""
import pandas as pd
import numpy as np

def remove_duplicates(df, subset=None, keep='first'):
    before = len(df)
    df_clean = df.drop_duplicates(subset=subset, keep=keep)
    removed = before - len(df_clean)
    print(f"Removed {removed} duplicate rows")
    return df_clean

def handle_missing(df, strategy='mean', columns=None):
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    df_clean = df.copy()
    for col in columns:
        if strategy == 'mean':
            df_clean[col].fillna(df_clean[col].mean(), inplace=True)
        elif strategy == 'median':
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
        elif strategy == 'mode':
            df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
        elif strategy == 'drop':
            df_clean.dropna(subset=[col], inplace=True)
    
    print(f"Handled missing values in {len(columns)} columns using {strategy}")
    return df_clean

def detect_outliers(df, columns=None, method='iqr', threshold=1.5):
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    outlier_info = {}
    for col in columns:
        if method == 'iqr':
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - threshold * IQR
            upper = Q3 + threshold * IQR
            outliers = df[(df[col] < lower) | (df[col] > upper)]
            outlier_info[col] = len(outliers)
    
    return outlier_info

def summarize(df):
    print(f"Shape: {df.shape}")
    print(f"\\nColumn types:\\n{df.dtypes}")
    print(f"\\nMissing values:\\n{df.isnull().sum()}")
    print(f"\\nBasic stats:\\n{df.describe()}")
    return df.info()
