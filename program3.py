# Write multiple line of text in mylife.txt
# Ask for user input to add lines of text in mylife.txt

# Open mylife.txt file
with open("mylife.txt", "w") as file:

    # Ask for user input to add lines of text in mylife.txt
    while True:

        # Ask the user to enter a line
        enter_line = input("Enter line: ")
        
        # Confirm if the user still wants to add another line
        continue_adding = input("Are there more lines? (y/n)? ")

        # If user input is n, write the line to the file and break
        if continue_adding.lower() == "n":
            file.write(enter_line + "\n")
            break
        
        # If user input is y, write the line to the file
        else:
            file.write(enter_line + "\n")