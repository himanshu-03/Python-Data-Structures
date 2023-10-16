# Program Name: student_records.py
# Managing student records using data structures

# Initialize an empty dictionary to store student records
student_records = {}

# Function to add a new student record
def add_student():
    name = input("Enter student's name: ")
    course = input("Enter student's course: ")
    grade = input("Enter student's grade: ")
    
    student_records[name] = {'Course': course, 'Grade': grade}
    print(f"{name}'s record added successfully.\n")

# Function to display all student records
def display_students():
    if not student_records:
        print("No student records found.\n")
    else:
        print("Student Records:\n")
        for name, data in student_records.items():
            print(f"Name: {name}, Course: {data['Course']}, Grade: {data['Grade']}")
        print()

# Main program loop
while True:
    print("Choose an option:")
    print("1. Add a student record")
    print("2. Display all student records")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3).\n")

