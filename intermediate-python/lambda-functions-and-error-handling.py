file_size = 2500
extra_space = 0.15

# Define a lambda function
calculate_total = lambda x: x * (1 + extra_space)

# Call the lambda function
print(calculate_total(file_size))

file_size = 2500

#Call a lambda function in one line
print((lambda x: x * (1 + extra_space))(file_size))

colleagues = ["Sarah Martinez", "Michael Chen", "Emily Brown"]

# Apply the lambda function to each colleague's name
cleaned = map(lambda x: x.replace(" ", "_").lower(), colleagues)

# Convert map object to list
cleaned_list = list(cleaned)
print(cleaned_list)

# Define the sales list
sales = [125.97, 84.32, 99.78 ,154.21, 78.50, 83.67, 111.13]

# Print the sales list
print(sales)


def clean_text(text):
    # Attempt to clean the text
    try:
        return text.replace(" ", "_").lower()
    # Run this code if an error occurs
    except :
        print("The clean_text() function expects a string as an argument, please check the data type provided!")
clean_text(187)


def clean_text(text):
    # Check the data type
    if type(text) == str:

        return text.replace(" ", "_").lower()
    else:
        # Return a TypeError error if the wrong data type was used
        raise TypeError("The clean_text() function expects a string as an argument, please check the data type provided!")


clean_text("User Name 187")