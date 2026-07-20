# python_project3
python_project3

# INTERNSHIP TASK 3: Data Analysis Project (Pandas)

## Overview
This project demonstrates data analysis skills using **Pandas** on a small
sales dataset (`sales_data.csv`). It covers loading and inspecting data,
cleaning missing or incorrect values, applying filtering/grouping/aggregation,
and summarizing the key insights in plain language.

## Goal
Demonstrate data analysis skills using Pandas.

## Requirements Covered
- Load and inspect a CSV dataset
- Clean missing or incorrect data
- Apply filtering, grouping, and aggregation
- Explain insights in simple words

## Technologies Used
- Python 3
- `pandas` library

## Dataset
`sales_data.csv` — a small sample dataset of 20 sales orders across three
categories (Electronics, Furniture, Stationery), containing some intentionally
messy data (missing values and one negative quantity) to demonstrate cleaning.

## How It Works
1. **Load & Inspect** — reads the CSV, prints the first rows, column info,
   and counts missing values.
2. **Clean** — fills missing Quantity/Price values, removes rows with
   invalid (negative) Quantity, and converts dates to proper datetime format.
3. **Filter, Group & Aggregate** — filters Electronics orders, and groups
   data by Category, Region, and Product to calculate totals and averages.
4. **Insight Summary** — prints a short, plain-English summary of the key
   findings from the analysis.

## Installation
```
pip install pandas
```

## Running the Project
Make sure `sales_data.csv` is in the same folder as the script, then run:
```
python data_analysis.py
```

## Example Insight Summary Output
```
1. 'Electronics' is the best-selling category by total sales value,
   contributing ₹225,184 in revenue.

2. The 'North' region generated the highest total sales value,
   at ₹159,396.

3. On average, 'Pen' is ordered in the highest quantity per order
   (35.0 units), suggesting it's a popular, frequently bought item.

4. Two rows had missing Quantity or Price values, and one row had a
   negative Quantity (a data entry error). These were cleaned before
   analysis to avoid skewing the results.
```

## Learning Outcomes
This project helped me understand:
- Loading and inspecting data with Pandas
- Identifying and handling missing/invalid data
- Using `groupby()` and aggregation functions
- Filtering DataFrames based on conditions
- Turning raw analysis into clear, readable insights

## Author
**Swayam N Gowda**
Python Developer 

## License
This project is created for educational and learning purposes.
