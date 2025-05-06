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

    def __init__(self,filename):
        self.filename = filename        
        self.tasks = []


    def load_tasks(self):
        if not self.tasks:
            print("ToDo List is empty!\n")
            return

        try:
            with open(self.filename, mode="r", newline="") as f_in:
                reader = csv.reader(f_in)
                next(reader)    # for pass headers
                for row in reader:
                    if len(row) == 3:
                        name, description, priority = row
                        task = Task(name, description,priority)
                        self.tasks.append(task)
        
        except FileNotFoundError:
            print(f"file {self.filename} not found!\n")


    def add_task(self):
        print("Add a new Task")
        name = input("Enter Task name: ")
        description = input("Enter your task description: ")
        priority = input("Enter priority (High / Medium / Low): ")
        task = Task(name, description, priority)    # make a list of name, description, priority as a task
        self.tasks.append(task)
        
        # save task into csv file        
        with open(self.filename, mode="a", newline="") as f_out:
            writer = csv.writer(f_out)
            writer.writerow([task.name, task.description, task.priority])
        print("Task added successfully\n")


    def remove_task(self):
        if not self.tasks:
            print("ToDoList is empty!\n")
            return
        
        # use tabulate for better display tasks
        table = [[i+1, t.name, t.description, t.priority] for i, t in enumerate(self.tasks)]
        headers = ["#", "name", "description", "priority"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
            
        try:
            choice = int(input("Enter the number of the task to remove: "))    
            if 1 <= choice <= len(self.tasks):
                removed = self.tasks.pop(choice - 1)
                print(f"removed: {removed.name}\n")    
            else:
                print("Invalid task number.\n")
            return
        
        except ValueError:
            print("Please Enter valid number.\n")
    
    
    def show_tasks(self):
        # use tabulate for better display tasks
        table = [[i+1, t.name, t.description, t.priority] for i, t in enumerate(self.tasks)]
        headers = ["#", "name", "description", "priority"]
        print(tabulate(table, headers=headers, tablefmt="grid"))




work_1 = ToDoList("tasks.csv")
work_1.add_task()
work_1.load_tasks()
work_1.remove_task()
work_1.show_tasks()
