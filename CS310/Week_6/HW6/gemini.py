slist = []  # Subject
clist = []  # Credit
glist = []  # Grade
id = input("Enter Student ID : ")
total_sub = int(input("\n Enter Total Subject : "))

# Create a dictionary to map grades to their corresponding grade points
grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0
}

for i in range(total_sub):
    subject = input(f"Enter Subject {i+1} > ")
    credit = int(input("Enter credit : "))
    grade = input("Enter grade : ").upper()
    print("=" * 50)

    # Input validation
    if grade not in grade_points:
        print("Invalid grade. Please enter a valid grade (A, B+, B, C+, C, D+, D, or F).")
        continue  # Skip to the next iteration
    if credit <= 0:
        print("Invalid credit hours. Please enter a positive integer.")
        continue  # Skip to the next iteration

    # Add data into the list
    slist.append(subject)
    clist.append(credit)
    glist.append(grade)

stotal = 0
ctotal = 0
for i in range(total_sub):
    # Get the grade point from the dictionary
    grade_point = grade_points.get(glist[i], 0.0)  # Default to 0.0 if grade is not found
    stotal += grade_point * clist[i]
    ctotal += clist[i]

# Display the output
print('Student ID : ', id)
for i in range(total_sub):
    print(f"{slist[i]:<40} {clist[i]:<7} {glist[i]:<7}")
print("=" * 50)
print(f"{'GPA':>25} : {stotal / ctotal:0.2f}")
print("=" * 50)
