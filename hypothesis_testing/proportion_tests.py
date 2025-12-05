import pandas as pd
from scipy.stats import t
import matplotlib.pyplot as plt
import pingouin as pg
import seaborn as sns

def load_dataset(file_path):

    return pd.read_feather(file_path)

# load dataset Stack Overflow
stack_overflow = load_dataset("../data/stack_overflow.feather")

# load dataset Late Shipments
late_shipments = load_dataset("../data/late_shipments.feather")

# load dataset US Democrat vote
sample_dem_data = load_dataset("../data/dem_votes_potus_12_16.feather")

# load dataset US Republican vote
us_republican_vote = load_dataset("../data/repub_votes_potus_08_12.feather")

# Hypothesize that the proportion of late shipments is 6%
p_0 = 0.06

# Calculate the sample proportion of late shipments
p_hat = (late_shipments["late"] == "Yes").mean()

# Calculate the sample size
n = len(late_shipments)

# Print p_hat and n
print(p_hat, n)

# Calculate the numerator and denominator of the test statistic
numerator = p_hat - p_0
denominator = ((p_0 * (1 - p_0)) / n) ** 0.5

# Calculate the test statistic
z_score = numerator / denominator

# Print the result
print(z_score)

# Calculate the p-value from the z-score
p_value = 1 - norm.cdf(z_score)

# Print the p-value
print(p_value)

# Calculate the pooled estimate of the population proportion
p_hat = (late_shipments["late"] == "Yes").mean()

# Print the result
print(p_hat)

# Calculate the pooled estimate of the population proportion
p_hat = (p_hats["reasonable"] * ns["reasonable"] + p_hats["expensive"] * ns["expensive"]) / (ns["reasonable"] + ns["expensive"])

# Calculate p_hat one minus p_hat
p_hat_times_not_p_hat = p_hat * (1 - p_hat)

# Divide this by each of the sample sizes and then sum
p_hat_times_not_p_hat_over_ns = p_hat_times_not_p_hat / ns["expensive"] + p_hat_times_not_p_hat / ns["reasonable"]

# Calculate the standard error
std_error = np.sqrt(p_hat_times_not_p_hat_over_ns)

# Calculate the z-score
z_score = (p_hats["expensive"] - p_hats["reasonable"]) / std_error

# Print z_score
print(z_score)

# Calculate the z-score
z_score = (p_hats["expensive"] - p_hats["reasonable"]) / std_error

# Calculate the p-value from the z-score
p_value = 1 - norm.cdf(z_score)

# Print p_value
print(p_value)

# Count the late column values for each freight_cost_group
late_by_freight_cost_group = late_shipments.groupby("freight_cost_group")["late"].value_counts()

# Print the counts
print(late_by_freight_cost_group)

# Count the late column values for each freight_cost_group
late_by_freight_cost_group = late_shipments.groupby("freight_cost_group")['late'].value_counts()

# Create an array of the "Yes" counts for each freight_cost_group
success_counts = np.array([
    late_by_freight_cost_group["expensive"]["Yes"],
    late_by_freight_cost_group["reasonable"]["Yes"]
])

# Create an array of the total number of rows in each freight_cost_group
n = np.array([
    late_shipments["freight_cost_group"].value_counts()["expensive"],
    late_shipments["freight_cost_group"].value_counts()["reasonable"]
])

# Run a z-test on the two proportions
from statsmodels.stats.proportion import proportions_ztest
stat, p_value = proportions_ztest(success_counts, n, alternative="larger")

# Print the results
print(stat, p_value)


