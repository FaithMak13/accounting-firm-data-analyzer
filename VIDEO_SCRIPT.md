# 4–5 Minute Video Script

## 0:00–0:30 — Introduction

Hello, my name is Faith Makawure. For this project, I created an Accounting Firm Data Analyzer using Python.

The purpose of this program is to analyze employee information for a fictional accounting firm with 40 employees. The employees are divided into four departments: Secretarial, Accounting, Trusts and Estates, and Audit and Clerks.

## 0:30–1:15 — Explain the Dataset

The employee data is stored in a CSV file called employees.csv.

Each record contains an employee ID, employee name, department, position, monthly salary, years of service, and number of training courses completed.

I created the dataset specifically for this project, so it does not contain real employee information.

## 1:15–2:15 — Run the Program

Now I will run the Python program.

The program loads the CSV file using pandas. It then calculates the total monthly payroll, average salary, highest salary, and lowest salary.

It also creates a department summary showing the number of employees, average salary, total payroll, and average years of service.

The program also answers three questions:
1. Which department has the most employees?
2. Which department has the highest average salary?
3. How many employees have completed at least two training courses?

## 2:15–3:30 — Walk Through the Code

The first important function is load_data. This function reads the CSV file into a pandas DataFrame.

The analyze_data function performs the main calculations. I use sum and mean to calculate payroll and average salary. I also use groupby to organize the information by department.

Another important section identifies the highest-paid employee using the employee's salary.

I separated the program into functions because this makes the code easier to understand, test, and maintain.

## 3:30–4:20 — Explain the Charts

The program creates two charts.

The first chart compares average monthly salary between departments.

The second chart shows how many employees work in each department.

These visualizations make it easier to understand the information instead of looking only at numbers.

## 4:20–5:00 — Conclusion

In conclusion, this project helped me learn how Python can be used for practical data analysis.

I learned how to work with CSV files, pandas DataFrames, functions, calculations, grouping data, and matplotlib charts.

The same type of analysis could be adapted for a real accounting firm to help management understand staffing, payroll, training, and departmental information.

Thank you for watching my project demonstration.
