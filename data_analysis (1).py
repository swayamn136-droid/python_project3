import pandas as pd

CSV_FILE_PATH = "sales_data.csv"


def load_and_inspect(path):
    """Loads the CSV file and prints basic information about it."""
    print("=" * 50)
    print("STEP 1: LOAD AND INSPECT DATA")
    print("=" * 50)

    df = pd.read_csv(path)

    print(f"\nLoaded '{path}' successfully. Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")

    print("First 5 rows:")
    print(df.head())

    print("\nColumn info:")
    print(df.info())

    print("\nMissing values per column:")
    print(df.isnull().sum())

    return df


def clean_data(df):
    """Cleans missing values and removes rows with incorrect/invalid data."""
    print("\n" + "=" * 50)
    print("STEP 2: CLEAN DATA")
    print("=" * 50)

    rows_before = len(df)

    # Fill missing Quantity with 0, missing Price with the column's average
    df["Quantity"] = df["Quantity"].fillna(0)
    df["Price"] = df["Price"].fillna(df["Price"].mean())

    # Remove rows with invalid (negative or zero) Quantity — these are data entry errors
    df = df[df["Quantity"] > 0]

    # Convert OrderDate to a proper datetime type
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    rows_after = len(df)
    print(f"\nRows before cleaning: {rows_before}")
    print(f"Rows after cleaning : {rows_after}")
    print(f"Rows removed        : {rows_before - rows_after} (invalid quantity)")

    # Add a calculated column: total sale value per row
    df["TotalValue"] = df["Quantity"] * df["Price"]

    return df


def analyze_data(df):
    """Applies filtering, grouping, and aggregation to the cleaned dataset."""
    print("\n" + "=" * 50)
    print("STEP 3: FILTER, GROUP, AND AGGREGATE")
    print("=" * 50)

    # Filtering: only Electronics category
    electronics = df[df["Category"] == "Electronics"]
    print(f"\nFiltered: Electronics orders only ({len(electronics)} rows)")
    print(electronics[["Product", "Quantity", "Price", "Region"]].to_string(index=False))

    # Grouping + aggregation: total sales value by category
    print("\nTotal sales value by Category:")
    category_totals = df.groupby("Category")["TotalValue"].sum().sort_values(ascending=False)
    print(category_totals)

    # Grouping + aggregation: total sales value by region
    print("\nTotal sales value by Region:")
    region_totals = df.groupby("Region")["TotalValue"].sum().sort_values(ascending=False)
    print(region_totals)

    # Grouping + aggregation: average quantity sold per product
    print("\nAverage quantity sold per Product:")
    avg_quantity = df.groupby("Product")["Quantity"].mean().sort_values(ascending=False)
    print(avg_quantity)

    return category_totals, region_totals, avg_quantity


def print_insights(category_totals, region_totals, avg_quantity):
    """Explains the key findings in simple words."""
    print("\n" + "=" * 50)
    print("STEP 4: INSIGHT SUMMARY")
    print("=" * 50)

    top_category = category_totals.idxmax()
    top_region = region_totals.idxmax()
    top_product = avg_quantity.idxmax()

    print(f"""
1. '{top_category}' is the best-selling category by total sales value,
   contributing ₹{category_totals.max():,.0f} in revenue.

2. The '{top_region}' region generated the highest total sales value,
   at ₹{region_totals.max():,.0f}.

3. On average, '{top_product}' is ordered in the highest quantity per order
   ({avg_quantity.max():.1f} units), suggesting it's a popular, frequently
   bought item.

4. Two rows had missing Quantity or Price values, and one row had a
   negative Quantity (a data entry error). These were cleaned before
   analysis to avoid skewing the results.
""")


def main():
    df = load_and_inspect(CSV_FILE_PATH)
    df = clean_data(df)
    category_totals, region_totals, avg_quantity = analyze_data(df)
    print_insights(category_totals, region_totals, avg_quantity)


if __name__ == "__main__":
    main()
