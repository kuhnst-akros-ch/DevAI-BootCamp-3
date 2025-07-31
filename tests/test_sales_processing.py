import pandas as pd
from src.parse_sales_data import parse_sales_data
from src.calculate_monthly_aggregates import calculate_monthly_aggregates

def test_parse_sales_data(tmp_path):
    csv_file = tmp_path / "sales.csv"
    csv_file.write_text("date,amount\n2024-01-01,100\n2024-01-15,200")
    df = parse_sales_data(str(csv_file))
    assert isinstance(df, pd.DataFrame)
    assert 'date' in df.columns
    assert 'amount' in df.columns

def test_calculate_monthly_aggregates():
    data = {'date': pd.to_datetime(['2024-01-01', '2024-01-15', '2024-02-01']),
            'amount': [100, 200, 300]}
    df = pd.DataFrame(data)
    monthly_agg = calculate_monthly_aggregates(df)
    assert 'year_month' in monthly_agg.columns
    assert 'total_sales' in monthly_agg.columns
    assert monthly_agg.shape[0] == 2