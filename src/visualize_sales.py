from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt


def plot_monthly_sales(df: pd.DataFrame, output_path: Optional[str] = None) -> None:
    """
    Plots monthly sales from a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with 'year_month' and 'total_sales' columns.
        output_path (Optional[str]): Path to save the plot. If None, shows the plot.
    """
    plt.figure(figsize=(8, 4))
    plt.plot(df["year_month"].astype(str), df["total_sales"], marker="o")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.title("Monthly Sales")
    plt.tight_layout()
    if output_path is not None:
        plt.savefig(output_path)
        print(f"Plot saved to: {output_path}")
    else:
        plt.show()
