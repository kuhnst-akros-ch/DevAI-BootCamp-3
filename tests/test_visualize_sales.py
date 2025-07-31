python
import pandas as pd
from src.visualization import plot_monthly_sales


def test_plot_monthly_sales(monkeypatch) -> None:
    # Monkeypatch plt.show to avoid opening a window during tests
    import matplotlib.pyplot as plt
    monkeypatch.setattr(plt, "show", lambda: None)
    data = {
        "month": ["2024-01", "2024-02"],
        "sales": [250, 200]
    }
    df = pd.DataFrame(data)
    plot_monthly_sales(df, "month", "sales")
