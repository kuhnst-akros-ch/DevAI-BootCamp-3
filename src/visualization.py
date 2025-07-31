python
from typing import Any
import matplotlib
import sys


def ensure_gui_backend() -> None:
    gui_backends = ["Qt5Agg", "TkAgg"]
    current_backend: str = matplotlib.get_backend()
    if current_backend.lower() == "agg":
        for backend in gui_backends:
            try:
                matplotlib.use(backend)
                import matplotlib.pyplot as plt  # type: ignore
                return
            except Exception:
                continue
        raise RuntimeError("No GUI backend available for matplotlib. Install PyQt5 or tk.")


def plot_monthly_sales(monthly_df: Any, month_col: str, sales_col: str) -> None:
    ensure_gui_backend()
    import matplotlib.pyplot as plt  # type: ignore
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_df[month_col].astype(str), monthly_df[sales_col])
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Monthly Sales")
    plt.tight_layout()
    plt.show()
