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

# Get the students with the highest GWA
highest_gwa = min(student_gwa.values())

# Find the names of the students with the highest GWA
students = [name for name, gwa in student_gwa.items() if gwa == highest_gwa]

# Output the names of the students with the highest GWA
if len(students) == 1:
    print(f"The student with the highest GWA is {students[0]} with a GWA of {highest_gwa}")
else:
    print(f"The students with the highest GWA are {', '.join(students)} with a GWA of {highest_gwa}")