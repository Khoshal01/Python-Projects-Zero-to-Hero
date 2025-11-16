
def check(user_name,password):
    correct_name = "khoshal amin"

    correct_password ="Python@123"

    if correct_name != user_name:
        return False
    elif password != correct_password:
        return False
    elif correct_name == user_name and correct_password == password:
        return True
    return False
    

def valid_password(password):
    special = "@#$%^&*()"

    while True:
        if len(password) < 8:
            
            password = input("Enter the correct len Password:- ")
            continue
        if  not any(ch.isupper() for ch in password):
            password = input("Use an upsercase cha:- ")
            continue
        
        if not any(ch in special for ch in password):
            password = input("Add any speacial char in password:- ")
            continue
        
        return password


    


user_name = input("UserName:- ")
password = input("Password:- ")
password = valid_password(password)

if check(user_name,password):
    print("Welcome")
else:
    print("Incrorrect password or username")



    






