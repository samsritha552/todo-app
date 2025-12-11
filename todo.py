tasks = []


def show_menu():
    print("\n===== TO-DO LIST APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print("==========================")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            remove_id = int(input("Enter task number to remove: "))
            if 1 <= remove_id <= len(tasks):
                tasks.pop(remove_id - 1)
                print("Task removed!")
            else:
                print("Invalid task number.")

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
