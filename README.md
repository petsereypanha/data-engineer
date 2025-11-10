# Data Engineering Learning Repository

A comprehensive collection of Python scripts and examples focused on data engineering fundamentals, including data importing, manipulation, API interactions, and Python programming concepts.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Topics Covered](#topics-covered)
- [Data Files](#data-files)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains hands-on examples and exercises covering essential data engineering topics in Python. It includes practical implementations of data importing techniques, working with various file formats, API interactions, and intermediate Python programming concepts.

## 📁 Project Structure

```
data-engineer/
├── data/                                    # Sample datasets
│   ├── a_movie.json
│   ├── digits_header.txt
│   ├── digits.csv
│   ├── moby_dick.txt
│   ├── sales.csv
│   ├── seaslug.txt
│   ├── test.hdf5
│   ├── titanic_corrupt.txt
│   ├── titanic.csv
│   └── winequality-red.csv
├── importing-data-in-python/                # Data importing fundamentals
│   ├── importing-data.py
│   ├── introduction-and-flat-files.py
│   └── relational-databases.pyi
├── intermediate-importing-data/             # Advanced data importing
│   ├── diving-deep-into-the-Twitter-API.py
│   ├── importing-data-from-the-Internet.py
│   └── interacting-with-APIs.py
├── intermediate-python/                     # Python programming concepts
│   ├── function.py
│   ├── lambda-functions-and-error-handling.py
│   └── python-ecosystem.py
├── introduction-api/                        # API fundamentals
│   └── making-api-requests-with-python.py
├── introduction-to-python/                  # Python basics
│   ├── control-flow-and-loops.py
│   ├── data-types.py
│   └── introduction.py
├── scripts/                                 # Utility scripts
│   ├── generate_digits.py
│   ├── generate_h5py.py
│   └── numpy_txt.py
└── requirements.txt                         # Project dependencies
```

## 🛠 Technologies

- **Python 3.x**
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **PyYAML** - YAML file parsing
- **Pillow** - Image processing
- **Tweepy** - Twitter API integration

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/petsereypanha/data-engineer.git
cd data-engineer
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Navigate to any module directory and run the Python scripts:

```bash
# Example: Run data importing scripts
python importing-data-in-python/importing-data.py

# Example: Run API interaction scripts
python intermediate-importing-data/interacting-with-APIs.py

# Example: Run Python function examples
python intermediate-python/function.py
```

## 📚 Topics Covered

### Importing Data in Python
- Reading flat files (CSV, TXT)
- Working with Excel files
- Loading pickle files
- Importing SAS and Stata files
- Working with HDF5 files
- Loading MATLAB files

### Intermediate Importing Data
- Importing data from the Internet
- API interactions and authentication
- Working with Twitter API
- HTTP requests and responses
- JSON data parsing

### Intermediate Python
- Function definition and usage
- Default arguments and keyword arguments
- Docstrings and documentation
- `*args` and `**kwargs`
- Lambda functions
- Error handling
- Python ecosystem tools

### Introduction to Python
- Basic data types
- Control flow (if/else statements)
- Loops (for, while)
- Python fundamentals

### API Interactions
- Making HTTP requests
- RESTful API concepts
- Authentication methods
- Handling API responses

## 📊 Data Files

The `data/` directory contains various sample datasets for practice:

- **CSV files**: `digits.csv`, `sales.csv`, `titanic.csv`, `winequality-red.csv`
- **JSON files**: `a_movie.json`
- **Text files**: `moby_dick.txt`, `seaslug.txt`, `digits_header.txt`
- **HDF5 files**: `test.hdf5`
- **Specialized formats**: Various data formats for learning different import techniques

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is created for educational purposes.

## 👤 Author

**Panha Setserey**
- GitHub: [@petsereypanha](https://github.com/petsereypanha)

---

⭐ If you find this repository helpful, please consider giving it a star!
