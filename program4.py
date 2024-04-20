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

    # Check if number is even and square the number
    even_numbers = [number**2 for number in numbers if number % 2 == 0]

    # Write even numbers to double.txt
    with open('double.txt', 'w') as even_file:
        for number in even_numbers:
            even_file.write(str(number) + ' ')
    
    # Check if number is odd and cube the number
    odd_numbers = [number**3 for number in numbers if number % 2 != 0]

    # Write odd numbers to triple.txt
    with open('triple.txt', 'w') as odd_file:
        for number in odd_numbers:
            odd_file.write(str(number) + ' ')