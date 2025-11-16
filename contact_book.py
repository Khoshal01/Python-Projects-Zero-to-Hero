
import os


my_contact = []
def menu():
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Remove Contact")
    print("4. View Contacts")
    print("5. Exit")
    option = int(input("Enter any option:- "))
    return option  

def add_contact():
    name = input("Enter Contact name: ")
    phone = input("Enter Contact Phone Number: ")
    email = input("Enter COntact Email Address: ")

    contact = {
        "name":name,
        "phone":phone,
        "email":email
    }

    my_contact.append(contact)
    print("Added succefully")


def search_contact(name):
    for contact in my_contact:
        if contact["name"].lower() == name.lower():
            print(contact)
            return 
    print("N0 Contact with this name.....")

def remove_contact(name):
    for conatct in my_contact:
        if conatct["name"].lower() == name.lower():
            my_contact.remove(conatct)
            print("Contact Deleted Successfully")
            return
    print("N0 Contact with this name.....")


def view_contact():
    if not my_contact:
        print("No contact to show")

    for contact in my_contact:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("---------------------------")


    







option = menu()
while True:
    if option == 1:
        add_contact() 

    elif option == 2:
        name = input("Enter contact name: ").lower()
        search_contact(name) 
        input("Enter any button to continue.....")
    elif option == 3:
        name = input("Enter contact name: ").lower()
        remove_contact(name)  
        input("Enter any button to continue....")
    elif option == 4:
        view_contact() 
        input("Enter any button to continue.....")
    else:
        print("Exit")
        break
    os.system("cls")
    option = menu()

