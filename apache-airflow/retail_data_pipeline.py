import pandas as pd
import os

# Extract function is already implemented for you
def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on = "index")
    return merged_df

# Call the extract() function and store it as the "merged_df" variable
merged_df = extract(grocery_sales, "extra_data.parquet")


def transform(raw_data):
    # Step 1: Fill missing numerical values (using mean for simplicity/choice)
    # Identify numerical columns (excluding 'index' used for merging, and 'IsHoliday' which is a flag)
    # The columns with potential NaNs based on the description are likely the MarkDown columns, CPI, and Unemployment, but we'll apply it broadly to float columns.
    numerical_cols = raw_data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    # Exclude 'IsHoliday' if it was loaded as int/float, and 'index', 'Store_ID' as they are identifiers
    cols_to_fill = [col for col in numerical_cols if col not in ['index', 'Store_ID', 'IsHoliday']]

    # Fill NaN values with the mean of the column
    for col in cols_to_fill:
        raw_data[col].fillna(raw_data[col].mean(), inplace=True)

    # Step 2: Add a column "Month"
    # Convert 'Date' to datetime objects first to extract the month
    raw_data['Date'] = pd.to_datetime(raw_data['Date'])
    raw_data['Month'] = raw_data['Date'].dt.month.astype(float)

    # Step 3: Keep rows where the weekly sales are over $10,000
    transformed_df = raw_data[raw_data['Weekly_Sales'] > 10000]

    # Step 4: Drop unnecessary columns.
    # The required columns for clean_data are: "Store_ID", "Month", "Dept", "IsHoliday", "Weekly_Sales", "CPI", "Unemployment"
    required_cols = ["Store_ID", "Month", "Dept", "IsHoliday", "Weekly_Sales", "CPI", "Unemployment"]

    # Drop columns not in the required list
    # Need to make sure all required columns exist before selecting
    # For robust code, we select only the required ones that are present
    final_cols = [col for col in required_cols if col in transformed_df.columns]

    clean_data = transformed_df[final_cols]

    return clean_data

# Call the transform() function and pass the merged DataFrame
clean_data = transform(merged_df)


def avg_weekly_sales_per_month(clean_data):
    # Select "Month" and "Weekly_Sales" columns
    agg_data = clean_data[["Month", "Weekly_Sales"]]

    # Group, aggregate (mean), reset index, and round
    agg_data = (
        agg_data.groupby("Month")['Weekly_Sales']
        .agg('mean')  # Calculate the average (mean)
        .reset_index(name='Avg_Sales')  # Rename the aggregated column to 'Avg_Sales'
        .round(2)  # Round the 'Avg_Sales' to two decimal places
    )

    # Note: reset_index(name='...') works directly to rename the aggregated series.
    # If using .rename(), it would look like:
    # .agg(Avg_Sales='Weekly_Sales').reset_index()

    return agg_data

# Call the avg_weekly_sales_per_month() function and pass the cleaned DataFrame
agg_data = avg_weekly_sales_per_month(clean_data)


# 3. Create the load() function
def load(full_data, full_data_file_path, agg_data, agg_data_file_path):
    # Save the cleaned DataFrame
    full_data.to_csv(full_data_file_path, index=False)

    # Save the aggregated DataFrame
    agg_data.to_csv(agg_data_file_path, index=False)

    # Return a success message or the file paths
    return f"DataFrames successfully saved to {full_data_file_path} and {agg_data_file_path}"

# Call the load() function and pass the cleaned and aggregated DataFrames with their paths
load(clean_data, "clean_data.csv", agg_data, "agg_data.csv")


# 4. Define a validation() function
def validation(file_path):
    # Check if the file exists in the current working directory
    is_present = os.path.exists(file_path)

    if is_present:
        print(f"✅ Validation successful: The file '{file_path}' exists.")
    else:
        print(f"❌ Validation failed: The file '{file_path}' was not found.")

    return is_present

# Call the validation() function and pass first, the cleaned DataFrame path, and then the aggregated DataFrame path
# 1. Call validation for the cleaned DataFrame path
validation("clean_data.csv")

# 2. Call validation for the aggregated DataFrame path
validation("agg_data.csv")