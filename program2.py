# Read a file that contains the name and GWA of 20 students
# Output the name of student who got the highest GWA

# Open student_gwa.txt file
with open("student_gwa.txt", "r") as file:

    # Read the content of the file
    content = file.readlines()

# Store the name and GWA of each student in a dictionary
student_gwa = {}

# Loop through the content of the file
for line in content:

    # Split the line into name and GWA
    name, gwa = line.split()

    # Store the name and GWA in the dictionary
    student_gwa[name] = float(gwa)

