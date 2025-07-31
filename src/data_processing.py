python
from typing import List, Dict
import pandas as pd


def read_sales_csv(filepath: str) -> pd.DataFrame:
    try:
        df: pd.DataFrame = pd.read_csv(filepath)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to read CSV: {e}")


def monthly_aggregates(df: pd.DataFrame, date_col: str, sales_col: str) -> pd.DataFrame:
    df[date_col] = pd.to_datetime(df[date_col])
    df['month'] = df[date_col].dt.to_period('M')
    monthly: pd.DataFrame = df.groupby('month')[sales_col].sum().reset_index()
    return monthly
