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

    # Check if number is even
    even_numbers = [number for number in numbers if number % 2 == 0]

    # Write even numbers to even.txt
    with open('even.txt', 'w') as even_file:
        for number in even_numbers:
            even_file.write(str(number) + ' ')
    
    print('Even numbers:', even_numbers)
    
    # Check if number is odd
    odd_numbers = [number for number in numbers if number % 2 != 0]

    # Write odd numbers to even.txt
    with open('odd.txt', 'w') as odd_file:
        for number in odd_numbers:
            odd_file.write(str(number) + ' ')
    
    print('Odd numbers:', odd_numbers)