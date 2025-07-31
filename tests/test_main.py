import sys
from src.__main__ import main

def test_main_cli(monkeypatch):
    monkeypatch.setattr(sys.stdin, "isatty", lambda: False)
    # You may need to mock parse_sales_data and plot_monthly_sales for full isolation
    # This is a placeholder for integration testing
    assert callable(main)