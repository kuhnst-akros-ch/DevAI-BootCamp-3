import pytest
import pandas as pd
from src.parse_sales_data import parse_sales_data


def test_parse_sales_data_file_not_found():
    with pytest.raises(ValueError):
        parse_sales_data("nonexistent.csv")


def test_parse_sales_data_valid(tmp_path):
    csv_path: str = tmp_path / "sales.csv"
    csv_path.write_text("date,sales\n2024-01-01,100\n2024-01-02,200")
    df: pd.DataFrame = parse_sales_data(str(csv_path))
    assert not df.empty
    assert "date" in df.columns
