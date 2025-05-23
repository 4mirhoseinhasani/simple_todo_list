# ✅ cmd-To-Do list (To-Do List in command-line)

A simple command-line To-Do List application built with **Object-Oriented Programming (OOP)** in Python. It lets users add, remove, view, save, and load tasks using a CSV file.

---

## 📁 Project Features

- Add a new task
- Remove a task by index
- View all current tasks
- Assign priorities to tasks (High / Medium / Low)
- Save the task list to a `.csv` file
- Load tasks from an existing `.csv` file
- Text-based menu for user interaction

---

## 🧱 Technologies & Concepts Used

- Python 3
- Object-Oriented Programming (OOP)
- CSV file handling
- Input/output with the console

---


## Challenges

### 1. How to Load Data from a CSV File

**The Challenge:**  
I needed to load tasks from a CSV file into my program so that previously saved tasks could be displayed and managed after restarting the app. At first, I wasn’t sure how to read the file correctly and convert each row into a usable task object.

**How I Solved It:**  
I used Python's built-in `csv` module and the `csv.reader` function to read each row from the file. Then I converted each row into a `Task` object and appended it to my task list (`self.tasks`).

**What I Learned:**  
I learned how to use `csv.reader` to iterate over rows in a CSV file and how to reconstruct objects (like `Task`) from raw CSV data.

---

### 2. How to Append Tasks to a CSV File

**The Challenge:**  
Initially, whenever I added a new task and saved it, all the previous tasks in the CSV file were being overwritten. I wanted to add only the new task without deleting the existing ones.

**How I Solved It:**  
I changed the file mode from `"w"` (write) to `"a"` (append) when opening the file with `open()`. This allowed me to write only the newly added task without affecting the previously saved data.

**What I Learned:**  
I learned the difference between file modes in Python (`"w"` vs `"a"`) and how to append new rows to a CSV file without overwriting the existing content.
#