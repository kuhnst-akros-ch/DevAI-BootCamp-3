import sys
import os
from src.parse_sales_data import parse_sales_data
from src.calculate_monthly_aggregates import calculate_monthly_aggregates
from src.visualize_sales import plot_monthly_sales


def main() -> None:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_csv = os.path.join(project_root, "data", "input", "sales_data.csv")
    output_png = os.path.join(project_root, "data", "output", "monthly_sales.png")
    df = parse_sales_data(input_csv)
    monthly_agg = calculate_monthly_aggregates(df)
    interactive = hasattr(sys, 'ps1') or sys.stdin.isatty()
    if interactive:
        from matplotlib import pyplot as plt
        plot_monthly_sales(monthly_agg)
        plt.show()
    else:
        plot_monthly_sales(monthly_agg, output_path=output_png)


if __name__ == '__main__':
    main()
