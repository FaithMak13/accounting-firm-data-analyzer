"""
Accounting Firm Data Analyzer
Author: Faith Makawure

This program analyzes employee information for a fictional accounting firm.
It demonstrates Python data handling, calculations, functions, and visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "employees.csv"


def load_data(filename):
    """Load employee data from a CSV file."""
    return pd.read_csv(filename)


def analyze_data(df):
    """Calculate useful summary statistics for the accounting firm."""
    total_payroll = df["Monthly_Salary"].sum()
    average_salary = df["Monthly_Salary"].mean()
    highest_salary = df["Monthly_Salary"].max()
    lowest_salary = df["Monthly_Salary"].min()

    department_summary = (
        df.groupby("Department")
        .agg(
            Employees=("Employee_ID", "count"),
            Average_Salary=("Monthly_Salary", "mean"),
            Total_Payroll=("Monthly_Salary", "sum"),
            Average_Service=("Years_Service", "mean"),
        )
        .sort_values("Average_Salary", ascending=False)
    )

    return total_payroll, average_salary, highest_salary, lowest_salary, department_summary


def show_department_chart(summary):
    """Display average salary by department."""
    summary["Average_Salary"].plot(kind="bar", title="Average Monthly Salary by Department")
    plt.ylabel("Salary (R)")
    plt.xlabel("Department")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.show()


def show_employee_distribution(df):
    """Display the number of employees in each department."""
    df["Department"].value_counts().plot(
        kind="bar", title="Employees by Department"
    )
    plt.ylabel("Number of Employees")
    plt.xlabel("Department")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.show()


def main():
    """Run the complete analysis."""
    df = load_data(DATA_FILE)

    total, average, highest, lowest, summary = analyze_data(df)

    print("\nACCOUNTING FIRM DATA ANALYZER")
    print("=" * 40)
    print(f"Total employees: {len(df)}")
    print(f"Total monthly payroll: R{total:,.2f}")
    print(f"Average monthly salary: R{average:,.2f}")
    print(f"Highest monthly salary: R{highest:,.2f}")
    print(f"Lowest monthly salary: R{lowest:,.2f}")

    print("\nDEPARTMENT SUMMARY")
    print("=" * 40)
    print(summary.round(2).to_string())

    print("\nHIGHEST PAID EMPLOYEE")
    print("=" * 40)
    highest_employee = df.loc[df["Monthly_Salary"].idxmax()]
    print(
        f"{highest_employee['Employee_Name']} - "
        f"{highest_employee['Position']} - "
        f"R{highest_employee['Monthly_Salary']:,.2f}"
    )

    print("\nDATA ANALYSIS QUESTIONS")
    print("=" * 40)
    largest_department = df["Department"].value_counts().idxmax()
    highest_avg_department = summary["Average_Salary"].idxmax()

    print(f"1. Which department has the most employees? {largest_department}")
    print(
        "2. Which department has the highest average salary? "
        f"{highest_avg_department}"
    )
    print(
        "3. How many employees have completed at least two training courses? "
        f"{(df['Training_Courses'] >= 2).sum()}"
    )

    show_department_chart(summary)
    show_employee_distribution(df)


if __name__ == "__main__":
    main()
