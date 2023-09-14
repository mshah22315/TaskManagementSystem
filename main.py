from task import Task
from todolist import ToDoList

def main():
    todo_list = ToDoList()
    todo_list.load_tasks("data/tasks.json")

    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            new_task = Task(title, description)
            todo_list.add_task(new_task)
            print(f"Task '{title}' added!")

        elif choice == '2':
            tasks = todo_list.list_tasks()
            if tasks:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            else:
                print("No tasks in the list.")

        elif choice == '3':
            title = input("Enter task title to mark as completed: ")
            if todo_list.complete_task(title):
                print(f"Task '{title}' marked as completed.")
            else:
                print(f"Task '{title}' not found.")

        elif choice == '4':
            title = input("Enter task title to delete: ")
            if todo_list.delete_task(title):
                print(f"Task '{title}' deleted.")
            else:
                print(f"Task '{title}' not found.")

        elif choice == '5':
            todo_list.save_tasks("data/tasks.json")
            print("Exiting the To-Do List Manager.")
            break

if __name__ == "__main__":
    main()
