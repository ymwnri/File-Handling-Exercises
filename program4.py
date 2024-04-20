# Create double.txt containing the square of even numbers from integers.txt
# Create triple.txt containing the cube of odd numbers from integers.txt

# Open integers.txt file
with open('integers.txt', 'r') as numbers_file:

    # Read content of integers.txt file
    numbers = numbers_file.read()

    # Split the numbers into a list of string
    numbers = numbers.split()

    # Convert the list of string to list of integer
    numbers = [int(number) for number in numbers]