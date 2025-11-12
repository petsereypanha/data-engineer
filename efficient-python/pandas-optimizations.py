
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Team': ['PIT', 'PIT', 'PIT', 'PIT', 'PIT'],
    'League': ['NL', 'NL', 'NL', 'NL', 'NL'],
    'Year': [2012, 2011, 2010, 2009, 2008],
    'RS': [651, 610, 587, 636, 735],
    'RA': [674, 712, 866, 768, 884],
    'W': [79, 72, 57, 62, 67],
    'G': [162, 162, 162, 161, 162],
    'Playoffs': [0, 0, 0, 0, 0]
}
data2 = {
    'Team': ['SFG', 'SFG', 'SFG', 'SFG', 'SFG'],
    'League': ['NL', 'NL', 'NL', 'NL', 'NL'],
    'Year': [2012, 2011, 2010, 2009, 2008],
    'RS': [718, 570, 697, 657, 640],
    'RA': [649, 578, 583, 611, 759],
    'W': [94, 86, 92, 88, 72],
    'G': [162, 162, 162, 162, 162],
    'Playoffs': [1, 0, 1, 0, 0]
}
pit_df = pd.DataFrame(data)
giants_df= pd.DataFrame(data2)
# Iterate over pit_df and print each row
for index, row in pit_df.iterrows():
    print(row)
# Iterate over pit_df and print each index variable, row, and row type
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))
# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)
# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

# Create an empty list to store run differentials
run_diffs = []
# Write a for loop and collect runs allowed and runs scored for each row
for index, row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']

    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)

rangers_df = pd.DataFrame(data)
# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
  print(row)

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  print(i, year, wins)

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
    i = row.Index
    year = row.Year
    wins = row.W

    # Check if rangers made Playoffs (1 means yes; 0 means no)
    if row.Playoffs == 1:
        print(i, year, wins)

run_diffs = []
data3 = {
    'Team': ['NYY'] * 47,
    'League': ['AL'] * 47,
    'Year': [2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1971, 1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962],
    'RS': [804, 867, 859, 915, 789, 968, 930, 886, 897, 877, 897, 804, 871, 900, 965, 891, 871, 821, 733, 674, 603, 698, 772, 788, 797, 839, 758, 770, 709, 820, 734, 735, 831, 730, 681, 671, 641, 648, 680, 562, 536, 522, 611, 611, 730, 714, 817],
    'RA': [668, 657, 693, 753, 727, 777, 767, 789, 808, 716, 697, 713, 814, 731, 656, 688, 787, 761, 746, 777, 749, 792, 748, 758, 738, 660, 679, 703, 716, 662, 672, 582, 651, 575, 588, 623, 610, 641, 612, 587, 531, 621, 612, 604, 577, 547, 680],
    'W': [95, 97, 95, 103, 89, 94, 97, 95, 101, 101, 103, 95, 87, 98, 114, 96, 92, 88, 76, 71, 67, 74, 85, 89, 90, 97, 87, 91, 79, 103, 89, 100, 100, 97, 83, 89, 80, 81, 93, 80, 83, 72, 70, 77, 99, 104, 96],
    'G': [162, 162, 162, 162, 162, 162, 162, 162, 162, 163, 161, 161, 161, 162, 162, 162, 162, 162, 162, 162, 162, 161, 161, 162, 162, 161, 162, 162, 162, 162, 160, 163, 162, 159, 160, 162, 162, 162, 163, 162, 164, 163, 160, 162, 164, 161, 162],
    'Playoffs': [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
}
yankees_df = pd.DataFrame(data3)
# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)

    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)

def text_playoffs(num_playoffs):
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No'

# Gather sum of all columns
stat_totals = yankees_df.sum(numeric_only=True, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = yankees_df[['RS', 'RA']].sum(numeric_only=True, axis=0)
print(total_runs_scored)

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = yankees_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

# Display the first five rows of the DataFrame
print(yankees_df.head())

# Create a win percentage Series
win_percs = yankees_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
yankees_df['WP'] = win_percs
print(yankees_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(yankees_df[yankees_df['WP'] >= 0.50])

# Create a sample DataFrame
baseball_df = pd.DataFrame(data3)
def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]

    wins = row['W']
    games_played = row['G']

    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

baseball_df['WP'] = win_percs_list

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].to_numpy(), baseball_df['G'].to_numpy())

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())

def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].to_numpy(), baseball_df['RA'].to_numpy())
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())
