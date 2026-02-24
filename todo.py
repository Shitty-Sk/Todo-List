tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("choose: ")
    
    if choice == "1":
        print(tasks)
    elif choice == "2":
        task = input("Enter task :")
        tasks.append(task)
    elif choice == "3":
        index = int(input("Enter task number to delete: "))
        tasks.pop(index)
    elif choice == "4":
        print("Fuck Off")
        break
    else:
        print("Kelanechuda")