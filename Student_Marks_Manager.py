
import os


students = []
marks = []

def menu():
    print("1. Add a new student and marks")
    print("2. View all students and marks")
    print("3. Update a student’s marks")
    print("4. Delete a student")
    print("5. Show average marks")
    print("6. Exit")
    option = int(input("Enter any option:- "))
    return option  

def add_student_data():
    name = input("Enter Student name: ")
    student_marks = int(input("Enter Students marks: "))
    
    students.append(name)
    marks.append(student_marks)
    print("Added succefully")


def update_marks(name):
    if name in students:
        index = students.index(name)
        new_marks = int(input("Enter new Marks: "))
        marks[index] = new_marks
        print("Updated Successfully")
        return

    print("N0 Contact with this name.....")

def remove_student(name):
    if name in students:
        index = students.index(name)
        marks.pop(index)
        students.pop(index)
        print("Deleted successfully!")
        return 
    
    print("N0 Contact with this name.....")


def view_student_data():
    if not students :
        print("No Data to show")

    for i in range(len(students)):
        print("Name:", students[i])
        print("Marks:", marks[i])
        print("---------------------------")


def show_average():
    if not marks:
        print("No marks available.")
        return
    avg = sum(marks) / len(marks)
    print(f"Class average marks: {avg:.2f}")









option = menu()
while True:
    if option == 1:
        add_student_data() 

    elif option == 2:
        view_student_data() 
        input("Enter any button to continue.....")
    elif option == 3:
        name = input("Enter Student name: ")
        update_marks(name)  
        input("Enter any button to continue....")
    elif option == 4:
        name = input("Enter Student name: ")
        remove_student(name)  
        input("Enter any button to continue....")
    elif option == 5:
        show_average()
        input("Enter any button to continue....")
    else:
        break
    os.system("cls")
    option = menu()

