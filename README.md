# Overview

Accounting Firm Data Analyzer is a Python program used for analysis of information about employees at a fictional accounting firm which has 40 employees in four departments: Secretarial, Accounting, Trusts & Estates, and Audit & Clerks.

Data is kept in CSV format in employees.csv file. It has fictional information about employees with regard to the department where they work, monthly salary, time spent working in the company and number of training courses which have been completed. Dataset was developed for the purposes of the project and does not contain any real information about the employees. There is no dataset URL available.

As a developing software engineer, I wish to develop my skills in Python programming, data analysis, problem solving, and visualization of data. I am interested in learning how to turn raw data into useful information that could be used for making business decisions, especially those concerning accounting and human resources.

The aim of this software is to analyze employee data and give some useful insights concerning the staffing, salaries, payroll per departments, length of service, and employee training.

Video Demonstration 

This 4-5 minute video will contain introduction to the dataset, description of the problems that have been researched, demonstration of how the Python software operates, results of the research and explanation of key parts of the code. There will also be a talking head part of me demonstrating the project.

[Software Demo Video](https://youtu.be/HGP9ZdXV4qc)

# Data Analysis Results

This program performs an analysis of the given employee database and provides answers to seven essential questions related to the accounting firm.

Which department has the largest number of employees?

Answer: [Insert the name of the department having the largest number of employees.]

Which department has the highest average monthly salary?

Answer: [Insert the name of the department having the highest average monthly salary.]

How much does the firm pay its employees every month?

Answer: [Insert the total monthly salary paid by the firm.]

What is the average monthly salary?

Answer: [Insert the average monthly salary of all 40 employees.]

Who has the highest monthly salary among all the employees?

Answer: [Insert the name of the employee having the highest monthly salary and his/her salary].

Who has the lowest monthly salary among all the employees?

Answer: [Insert the name of the employee having the lowest monthly salary and his/her salary].

How many employees have taken part in at least two trainings?

Answer: [Insert the number of such employees].

Data Visualization

Charts are used in this program in order to provide more convenient analysis of the information.

# Development Environment

The Accounting Firm Data Analyzer was created using the following software and technologies:

Programming language: Python 3.

Code editor: Visual Studio Code.

Data analysis package: pandas.

Data visualization package: matplotlib.

File format: CSV (Comma-Separated Values).

Version control: Git and GitHub (if used).

Python programming language is used to write the source code and implement the analysis as functions. The pandas package reads the CSV file, builds a DataFrame with employee data, groups the data by departments and performs calculations. Matplotlib package is used to build charts and visualize the results.

Project Files

accounting_data_analysis.py — Source code of the main Python program.

employees.csv — File with dataset with information about 40 imaginary employees.

README.md — Documentation of the project.

requirements.txt — File with the list of required Python packages.

Running the Program

Install Python 3 on your computer.

Open the terminal window in the project folder.

Install the required Python packages by executing:

pip install -r requirements.txt

Execute the program by using:

python accounting_data_analysis.py

Examine the statistics and charts created by the program.

It is important to make sure that employees.csv file is located in the proper folder.

# Useful Websites

* [Python Documentation](http://docs.python.org/3/)
* [Pandas Documentantion](http://pandas.pydata.org/docs/)
* [Matplotlib Documentantion](http://matplotlib.org/stable/index/.html)
* [Python CSV Documentantion](http://docs.python.org/3/library/csv.html)
* [Visual Studio Code Documentantion](http://code.visualstudio.com/docs)
* [GitHub Documentantion](http://docs.github.com/en)

# Future Work

* Item 1: Make data validation better: Look for missing values, salary amount errors, and inconsistency in employee details.

* Item 2: Extend analysis: Include median salaries, salary ranges, and payroll analysis for each department.

* Item 3: Make visual representations better: Improve labeling and include graphs for each statistic.

* Item 4: Do length of service analysis: Find the average years of service and service years for each department.

* Item 5: Make training analysis better: Compare training completion percentages for each department.

* Item 6: Generate reports: Export the analysis data to CSV, Excel, or PDF file.

* Item 7: Improve user experience: Enable the user to choose which questions/statistics they want to do analysis on.

* Item 8: Make error handling better: Give helpful messages when there is an issue with dataset.




