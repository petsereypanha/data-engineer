# Import the package with a name that follows PEP 8
import text_analyzer,textAnalyzer,TextAnalyzer

# Import the two packages that follow the minimal package requirements
import package
import py_package

# Use help() to print information about each imported package
help(package)
help(py_package)

# Import needed functionality
from collections import Counter

def plot_counter(counter, n_most_common=5):
  # Subset the n_most_common items from the input counter
  top_items = counter.most_common(n_most_common)
  # Plot `top_items`
  plot_counter_most_common(top_items)

def plot_counter_most_common(top_items):
    import matplotlib.pyplot as plt

    # Unzip `top_items` into two lists: `labels` and `values`
    labels, values = zip(*top_items)

    # Create a horizontal bar plot
    plt.barh(labels, values)
    plt.show()

# Import needed functionality
from collections import Counter

def sum_counters(counters):
  # Sum the inputted counters
  return sum(counters, Counter())

# Import local package
import text_analyzer

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = text_analyzer.sum_counters(word_counts)

# Plot word_count_totals using plot_counter from text_analyzer
text_analyzer.plot_counter(word_count_totals)

# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text analysis.',
      author='Your Name',
      packages=['text_analyzer'])

# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text analysis.',
      author='Your Name',
      packages=['text_analyzer'],
      install_requires=['matplotlib>=3.0.0'])

