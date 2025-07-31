import pandas as pd

def parse_sales_data(csv_path: str) -> pd.DataFrame:
    try:
        df: pd.DataFrame = pd.read_csv(csv_path)
        df['date'] = pd.to_datetime(df['date'])
        return df
    except Exception as e:
        raise ValueError(f"Error parsing CSV: {e}")