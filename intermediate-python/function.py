import string

full_name = "Alan Turing"

# Define the generate_email function
def generate_email(full_name):
    name_parts = full_name.split()
    email = name_parts[0].lower() + '.' + name_parts[1].lower() + '@techcompany.com'

# Return the email address
    return email

# Call the function on the full_name string
print(generate_email(full_name))

test_durations = [245.50, 189.99, 312.75, 156.20, 428.90, 201.35, 167.80]


# Complete the function
def test_report(durations):
    num_tests = len(durations)

    # Calculate total test time
    total_time = sum(durations)

    print("=== Test Report ===")
    print("Total Tests: ", num_tests)
    print("Total Execution Time (s): ", total_time)


# Generate the report for recent test runs
test_report(test_durations)


def validate_password(password):
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        # Check if password contains a special character
        for char in password:
            if char in string.punctuation:
                return True
    return False

# Call the function and store the result
is_valid = validate_password("Passw0rd!")  # Replace with the desired password to test
print("Is the password valid? ", is_valid)

product = 'Wireless Mouse'

# Define clean_text function
def clean_text(text, lower=True):
    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        # Apply lowercase transformation
        return clean_text.lower()

# Test with default behavior
print(clean_text(product))
original_price = 899.99


# Define the function with default arguments
def calculate_discount(price, discount_percent=15, round_result=True):
    discounted_price = price - (price * (discount_percent / 100))

    if round_result == True:
        # Round the result to two decimal places
        return round(discounted_price, 2)
    else:
        return discounted_price


# Call the function with keyword arguments
final_price = calculate_discount(price=original_price, round_result=False, discount_percent=25)
print(final_price)


def calculate_discount(price, discount_percent=15, round_result=True):
    # Add a single-line docstring
    """Calculate the discounted price of a product."""

    discounted_price = price - (price * (discount_percent / 100))
    if round_result == True:
        return round(discounted_price, 2)
    else:
        return discounted_price


#  Access the docstring
print(calculate_discount.__doc__)


def clean_text(text, lower=True):
    """
    Clean text by replacing spaces with underscores and optionally converting to lowercase.
    Args:
        text (str): A string to be cleaned.
        lower (bool): Whether to convert the text to lowercase.
    Returns:
        text (str): Cleaned string.
    """
    cleaned = text.replace(' ', '_')
    if not lower:
        return cleaned
    return cleaned.lower()


# Define a function called concat
def concat(*args):
  """Concatenates multiple string arguments with spaces between them."""

  result = ""

  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))


# Define a function called concat
def concat(**kwargs):
    """Concatenates keyword arguments into a single string with spaces."""

    result = ""

    # Iterate over the Python kwargs
    for kwarg in kwargs.values():
        result += " " + kwarg
    return result


# Call the function
print(concat(start="Python", middle="is", end="great!"))