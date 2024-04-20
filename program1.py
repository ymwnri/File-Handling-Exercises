# Read numbers.txt that contains 20 integers
# Create even.txt that will contain only the even numbers from numbers.txt
# Create odd.txt that will contain only the odd numbers from numbers.txt
# Print it in a list format

# Open numbers.txt
with open('numbers.txt', 'r') as numbers_file:

    # Read the intergers from the file as string
    numbers = numbers_file.read()

    # Split the numbers into a list of string
    numbers = numbers.split()

    # Convert the list of string to list of integer
    numbers = [int(number) for number in numbers] 