import pandas as pd

def calculate_monthly_aggregates(csv_path: str) -> pd.DataFrame:
    df: pd.DataFrame = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])
    df['year_month'] = df['date'].dt.to_period('M')
    monthly_agg: pd.DataFrame = df.groupby('year_month', as_index=False)['amount'].sum()
    monthly_agg.rename(columns={'amount': 'total_sales'}, inplace=True)
    return monthly_agg

if __name__ == '__main__':
    csv_file: str = 'sales_data.csv'
    monthly_aggregates: pd.DataFrame = calculate_monthly_aggregates(csv_file)
    print(monthly_aggregates)