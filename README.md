# Sales_Data_Analyzer9

# 📊 Sales Data Analyzer System

## 📌 Project Overview

The **Sales Data Analyzer System** is a menu-driven Python application developed using **Object-Oriented Programming (OOP)** concepts. The project is designed to analyze sales data stored in a CSV file using Python libraries such as **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**.

This application allows users to load datasets, clean missing values, perform statistical analysis, manipulate DataFrames, create pivot tables, generate different types of graphs, and save visualizations.

---

# 🎯 Objectives

The main objectives of this project are:

- Learn Object-Oriented Programming in Python.
- Perform data analysis using Pandas.
- Use NumPy for numerical computations.
- Visualize data using Matplotlib and Seaborn.
- Handle missing values in datasets.
- Understand statistical analysis of data.
- Create pivot tables for summarized reports.
- Build a menu-driven console application.

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Manipulation |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| CSV | Dataset Storage |

---

# 📁 Project Structure

```
Sales_Data_Analyzer/
│
├── main.py
├── sales_data_analyzer.py
├── sales_data.csv
├── README.md
```

---

# 📂 Dataset Information

The project uses a CSV dataset named:

```
sales_data.csv
```

The dataset contains the following columns:

| Column Name | Description |
|--------------|------------|
| OrderID | Unique Order ID |
| Date | Order Date |
| Region | Sales Region |
| SalesPerson | Sales Executive |
| Product | Product Name |
| Category | Product Category |
| Quantity | Quantity Sold |
| UnitPrice | Price Per Unit |
| TotalSales | Total Sales Amount |
| Profit | Profit Earned |

---

# 📚 Python Modules Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# 🏗 Class Used

```
SalesDataAnalyzer
```

---

# 🔹 Constructor

```python
__init__()
```

Purpose:

- Initializes the object.
- Creates dataset variable.
- Displays welcome message.

---

# 🔹 Destructor

```python
__del__()
```

Purpose:

- Displays farewell message when object is deleted.

---

# 📋 Features of the Project

## 1. Load Dataset

- Reads CSV file.
- Loads dataset into Pandas DataFrame.
- Displays success message.

---

## 2. Explore Dataset

Displays:

- First 5 Rows
- Last 5 Rows
- Column Names
- Data Types
- Dataset Information

Functions Used

```python
head()
tail()
columns
dtypes
info()
```

---

## 3. Handle Missing Values

Options:

- Show Missing Values
- Fill Missing Values
- Drop Missing Rows
- Replace Missing Values

Functions Used

```python
isnull()
fillna()
dropna()
```

---

## 4. NumPy Operations

Converts DataFrame into NumPy Array.

Operations:

- Shape
- Indexing
- Slicing
- First Row
- Last Row

Functions Used

```python
to_numpy()
shape
```

---

## 5. Mathematical Operations

Performs:

- Addition
- Subtraction
- Multiplication
- Division

---

## 6. Combine DataFrames

Operations:

- Concat
- Merge
- Join

Functions Used

```python
pd.concat()
pd.merge()
join()
```

---

## 7. Split DataFrame

Splits dataset using

```python
groupby()
```

---

## 8. Search, Sort and Filter

Operations:

- Search Record
- Sort Dataset
- Filter Dataset

Functions Used

```python
sort_values()
contains()
```

---

## 9. Aggregate Functions

Calculates:

- Sum
- Mean
- Maximum
- Minimum
- Count

Functions Used

```python
sum()
mean()
max()
min()
count()
```

---

## 10. Statistical Analysis

Calculates

- Mean
- Median
- Variance
- Standard Deviation
- Quantiles
- Description

Functions Used

```python
describe()
median()
std()
var()
quantile()
```

---

## 11. Pivot Table

Creates summarized report.

Function Used

```python
pivot_table()
```

---

## 12. Data Visualization

The project generates the following graphs:

### Bar Chart

Displays comparison between values.

### Line Chart

Shows trends over time.

### Scatter Plot

Displays relationship between two variables.

### Pie Chart

Displays percentage contribution.

### Histogram

Shows frequency distribution.

### Stack Plot

Displays cumulative values.

### Subplots

Shows multiple graphs together.

### Heatmap

Displays correlation between variables.

### Box Plot

Displays spread and outliers.

---

# 💾 Save Visualization

Generated graphs can be saved as

```
PNG
```

Example

```
sales_graph.png
```

---

# 📋 Menu Driven Interface

```
1. Load CSV Dataset

2. Explore Dataset

3. Handle Missing Values

4. NumPy Operations

5. Mathematical Operations

6. Combine DataFrames

7. Split DataFrame

8. Search / Sort / Filter

9. Aggregate Functions

10. Statistical Analysis

11. Create Pivot Table

12. Data Visualization

13. Exit
```

---

# ⚠ Exception Handling

The project uses Python Exception Handling for:

- Invalid File
- Wrong Input
- Invalid Column Name
- Empty Dataset
- Invalid Menu Choice

---

# ▶ How to Run

### Step 1

Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

---

### Step 2

Place all files in one folder.

```
main.py

sales_data_analyzer.py

sales_data.csv

README.md
```

---

### Step 3

Open Terminal

Run

```bash
python main.py
```

---

# 📈 Expected Output

The program displays a menu-driven interface where the user can:

- Load CSV Dataset
- Explore Data
- Perform Data Cleaning
- Analyze Data
- Generate Charts
- Save Charts
- Exit Program

---

# 🎓 Learning Outcomes

After completing this project, students will understand:

- Object-Oriented Programming
- Constructor & Destructor
- Pandas DataFrame
- NumPy Arrays
- Data Cleaning
- Statistical Analysis
- Pivot Tables
- Data Visualization
- Exception Handling
- CSV File Handling

---

# 👨‍💻 Developed By

**Name:** Nancy Rana

**Course:** Bachelor of Computer Applications (BCA)

**Project:** Sales Data Analyzer System

---

# 📜 Conclusion

The **Sales Data Analyzer System** is a complete data analysis application that demonstrates the use of Python programming, OOP concepts, NumPy, Pandas, Matplotlib, and Seaborn. It provides an easy-to-use interface for analyzing sales data and generating meaningful visualizations, making it an excellent academic project for learning data analysis and visualization techniques.

---

## ⭐ Thank You
