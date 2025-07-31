import pandas as pd

def calculate_monthly_aggregates(df: pd.DataFrame) -> pd.DataFrame:
    df['year_month'] = df['date'].dt.to_period('M')
    monthly_agg: pd.DataFrame = df.groupby('year_month', as_index=False)['amount'].sum()
    monthly_agg.rename(columns={'amount': 'total_sales'}, inplace=True)
    return monthly_agg