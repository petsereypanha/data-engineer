# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load student data
student_data = pd.read_csv('../data/student.csv')

# Change to use relplot() instead of scatterplot()
sns.scatterplot(x="absences", y="G3",
                data=student_data,
                kind="scatter",
                col="study_time",)

# Show plot
plt.show()


# Create a scatter plot of G1 vs. G3
sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col="schoolsup",
            row="famsup",
            col_order=["yes", "no"],
            row_order=["yes", "no"])

# Show plot
plt.show()

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

mpg = pd.read_csv('../data/mpg.csv')

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower",
    y="mpg",
    data=mpg,
    kind="scatter",
    size="cylinders",
    hue="cylinders")


# Show plot
plt.show()

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(
    x="acceleration",
    y="mpg",
    data=mpg,
    kind="scatter",
    hue="origin",
    style="origin"
)

# Show plot
plt.show()


