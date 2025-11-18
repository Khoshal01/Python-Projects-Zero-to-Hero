import os 
import json 


class DataBase:
    
    def __init__(self):
        self.tasks = []  # use lowercase for convention

    def save_data(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f, indent=4)  # use self.tasks

    
    def load_data(self):
        try:
            with open("tasks.json","r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        
    def view_tasks(self):
        tasks = self.load_data()
        if not tasks:
            print("NO data to show")
            return 
        for task in tasks:
            print("Task Name: ",task["name"])
            print("Task Status: ",task["status"])
        
        



    def add_task(self,taks_name,status):
        task = {"name":taks_name.lower(),"status":status}
        self.tasks.append(task)
        self.save_data()
        print("Done")
    
    def delete_data(self, task_name):
        tasks = self.load_data()
        for task in tasks:
            print("Hello")
            if task["name"].lower() == task_name.lower():
                self.tasks.remove(task)
                self.save_data()
                print("Task deleted!")
                return
        print("Task not found!")


    def done_tasks(self,task_name):
        self.tasks = self.load_data()
        for task in self.tasks:
            if task["name"] == task_name:
                task["status"] = "Done"
                self.save_data()
                print("Task has been marked as Done")
                return
        
        print("No data founded")

    

    






def menu():
    print("\n"+"="*100)
    print("\t"*10+"My TO-DO List")
    print("\n"+"="*100)
    print("I:- Add task")
    print("II:- View tasks")
    print("III:- Delete task")
    print("IV:- Mark task as done")
    print("V:- Save tasks to tasks.json")
    print("VI:- Load tasks on start")
    print("VII:- Nice clean menu")
    print("VIII:- Exit")
    option = int(input("Enter Your Option(1-8)"))
    return option


if __name__=='__main__':
    option = menu()
    db = DataBase()

    while True:
        if option == 1:
            os.system('CLS')
            name = input("Please Enter Task Name: ")
            status = input("Enter Task's Status(Done,pending): ")
            db.add_task(name.lower(),status.lower())
            input("Press any key to continue....")
            
        elif option == 2:
            os.system('CLS')
            db.view_tasks()
            input("Press any key to continue....")
        elif option == 3:
            os.system('CLS')
            name = input("Please Enter Task Name: ")
            db.delete_data(name.lower())
            input("Press any key to continue....")

        elif option == 4:
            os.system('CLS')
            name = input("Please Enter Task Name: ")
            db.done_tasks(name.lower())
            input("Press any key to continue....")

        elif option == 5:
            
            input("Press any key to continue....")
        elif option == 6 :
            os.system('CLS')
            db.load_data()
            print("Data Loaded!")
            input("Press any key to continue....")

        elif option == 7:
            os.system('CLS')
            option = menu()
            
        else:
            break

        option = menu()


    









