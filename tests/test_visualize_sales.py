import pandas as pd
import os
from src.visualize_sales import plot_monthly_sales


def test_plot_monthly_sales_saves_file_and_prints_path(tmp_path, capfd):
    data = {"year_month": ["2024-01", "2024-02"], "total_sales": [100, 200]}
    df = pd.DataFrame(data)
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    output_path = output_dir / "monthly_sales.png"
    plot_monthly_sales(df, output_path=str(output_path))
    assert os.path.isfile(output_path)
    out, _ = capfd.readouterr()
    assert f"Plot saved to: {output_path}" in out
