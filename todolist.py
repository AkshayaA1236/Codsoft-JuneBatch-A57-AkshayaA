from datetime import datetime

def main():
    tasks = []

    def show_menu():
        print("\nTO-DO LIST")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Exit")

    def add_task():
        n_tasks = int(input("\nHow many tasks do you want to add? "))
        for _ in range(n_tasks):
            task = input("Enter the task: ")
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tasks.append({"task": task, "done": False, "created_at": created_at, "updated_at": None})
            print("Task added!")

    def show_tasks():
        if not tasks:
            print("\nNo tasks to show.")
        else:
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                created_at = task["created_at"]
                updated_at = task["updated_at"] if task["updated_at"] else "Never"
                print(f"{index + 1}. {task['task']} - {status} (Created: {created_at}, Updated: {updated_at})")

    def mark_task_as_done():
        if not tasks:
            print("\nNo tasks to mark as done.")
            return
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["done"] = True
            tasks[task_index]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    def update_task():
        if not tasks:
            print("\nNo tasks to update.")
            return
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_index]["task"] = new_task
            tasks[task_index]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Task updated!")
        else:
            print("Invalid task number.")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            mark_task_as_done()
        elif choice == '4':
            update_task()
        elif choice == '5':
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
