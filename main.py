import os

class todolist:
    def __init__(list1):
        list1.tasks = []

    def display_tasks(list1):
        if not list1.tasks:
            print("No tasks found. Add some tasks to your to-do list.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(list1.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(list1, task):
        list1.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def remove_task(list1, index):
        if 1 <= index <= len(list1.tasks):
            removed_task = list1.tasks.pop(index - 1)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task index. Please provide a valid index.")

    def save_to_file(list1, filename="todolist.txt"):
        with open(filename, "w") as file:
            for task in list1.tasks:
                file.write(f"{task}\n")

    def load_from_file(list1, filename="todolist.txt"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                list1.tasks = [line.strip() for line in file.readlines()]
            print("To-Do List loaded successfully.")
        else:
            print("No saved To-Do List found.")

def main():
    todo_list = todolist()

    while True:
        print("\nMenu:")
        print("1. Display the To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save To-Do List to File")
        print("5. Load To-Do List from File")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "3":
            index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(index)
        elif choice == "4":
            filename = input("Enter the filename to save to(default: todolist.txt): ")
            todo_list.save_to_file(filename)
        elif choice == "5":
            filename = input("Enter the filename to load from(default: todolist.txt): ")
            todo_list.load_from_file(filename)
        elif choice == "6":
            print("Exiting program. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
