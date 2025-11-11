# load necessary libraries
import pandas as pd
# load banking data
banking = pd.read_csv('data/banking1.csv')
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'

# Print the header of account_opend
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Return missing value for error
                                           errors = 'coerce')

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])

# Import numpy
import numpy as np
import datetime as dt

# load banking data
banking = pd.read_csv('data/banking_dirty.csv')

# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])

# Store today's date
today = dt.date.today()

# If your dates are in a specific format, specify it
banking['birth_date'] = pd.to_datetime(banking['birth_date'], format='%Y-%m-%d')

# Calculate ages manually
ages_manual = today.year - banking['birth_date'].dt.year

# Check which rows have age matching manually calculated age
age_equ = banking['Age'] == ages_manual

# Filter banking into consistent and inconsistent ages
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Print number of inconsistent ages
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])