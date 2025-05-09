import csv
from tabulate import tabulate


class Task:
    # in this app tasks incloud 3 section: name, descriotion, priority (high / medium / low)
    def __init__(self,name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
    

    def __str__(self):
        return f"{self.name} | description: {self.description} | priority: {self.priority} "


class ToDoList:

    def __init__(self):        
        self.tasks = []    # a list fo save tasks into it


    def add_task(self):
        print("Add a new Task")
        # check  if name is empty
        while True:
            name = input("Enter Task name: ")
            if not name:
                print("name can not be empty!")
            else:
                break

        description = input("Enter your task description: ")
        if not description:    # default value for description
            description = "---"
        
        # priority validation
        valid_priorities = ['high', 'medium', 'low']
        while True:
            priority = input("Enter priority (High / Medium / Low): ").strip().lower()
            if priority not in valid_priorities:
                print("Invalid priority! please type high, medium or low: ")
            else:
                priority = priority.capitalize()
                break

        task = Task(name, description, priority)    # make a list of name, description, priority as a task
        self.tasks.append(task)
        print("Task added successfully")
        

    def remove_task(self):
        if not self.tasks:
            print("ToDoList is empty!")
            return
        # validity check of task number for remove
        while True:
            # use tabulate for better display tasks
            table = [[i+1, t.name, t.description, t.priority] for i, t in enumerate(self.tasks)]
            headers = ["#", "name", "description", "priority"]
            print(tabulate(table, headers=headers, tablefmt="grid"))
            
            try:
                choice = int(input("Enter the number of the task to remove: "))
            except ValueError:
                print("Please Enter valid number.")
                continue

            if 1 <= choice <= len(self.tasks):
                removed = self.tasks.pop(choice - 1)
                print(f"removed: {removed.name}\n")
                break                
            else:
                print(f"Invalid task number! please enter a number between 1 to {len(self.tasks)}")

    
    
    def show_tasks(self):
        if not  self.tasks:
            print("ToDoList in Empty!")
            return
        
        # use tabulate for better display tasks
        table = [[i+1, task.name, task.description, task.priority] for i, task in enumerate(self.tasks)]
        headers = ["#", "name", "description", "priority"]
        print(tabulate(table, headers=headers, tablefmt="grid"))


    def load_tasks_from_file(self, filename):
        try:
            with open(filename, mode="r", newline="") as f_in:
                reader = csv.reader(f_in)
                next(reader)    # for pass headers
                for row in reader:
                    name, description, priority = row
                    task = Task(name, description,priority)    # create suitable format for adding to list
                    self.tasks.append(task)
        
        except FileNotFoundError:
            print(f"file {filename} not found!")
            return


    def save_tasks_to_file(self, filename="result.csv"):
        try:
            with open(filename, mode='w', newline='') as f_out:
                writer = csv.writer(f_out)
                writer.writerow(["name", "description", "priority"])    # write headers 
                for task in self.tasks:
                    writer.writerow([task.name, task.description, task.priority])
        
        except ValueError:
            print("Please Enter valid name for file!")
            return


def show_menu():
    options = ['add Task', 'remove Task','show Tasks', 'load csv file', 'seve csv file', 'exit']
    table = [[i, item] for i, item in enumerate(options, start=1)]    # a list of items for the user to select
    headers = ['Options']
    print(tabulate(table, headers=headers, tablefmt='grid'))    # print in tabulate form
    choice = input("choose between 1 and 6: ")
    return choice


# user interface

print("Let's go to make a ToDoList! ")
todo = ToDoList()   # make a instance for ToDoList class

while True:
    choice = show_menu()
    try:
        if not choice.isdigit():
            print("please enter valid number between 1-6!")
            continue

        elif choice == '1':
            todo.add_task()

        elif choice == '2':
            todo.remove_task()

        elif choice == '3':
            todo.show_tasks()
            
        elif choice == '4':
            filename = input("Please enter csv file path for load task: ")
            todo.load_tasks_from_file(filename)

        elif choice == '5':
            res = input("do you want save in new file? (Y/N) ")
            
            if res.lower() == "y":
                filename = input("Please enter you file name: ")
                todo.save_tasks_to_file(filename)
            
            elif res.lower() == "n":
                todo.save_tasks_to_file()

        elif choice == '6':
            break
        
        else:
            print("please enter valid number between 1-6!")
            continue
    
    except Exception as e:
        print(f"Erorr {e}")
        break