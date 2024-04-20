# Write multiple line of text in mylife.txt
# Ask for user input to add lines of text in mylife.txt

# Open mylife.txt file
with open("mylife.txt", "w") as file:

    # Ask for user input to add lines of text in mylife.txt
    while True:

        # Ask the user to enter a line
        enter_line = input("Enter line: ")