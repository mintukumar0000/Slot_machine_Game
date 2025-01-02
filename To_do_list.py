def tasks(): #Function
    tasks = []
    print("---WELCOME TO THE TO-DO TASKS---")

    total_tasks = int(input("How many tasks you want to add= "))
    for i in range(1, total_tasks+1):
        tasks_name = input("Enter task {i} = ")
        tasks.append(tasks_name)
        print(f"Today's tasks are \n {tasks}")


        while True:
            operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
            if operation == 1:
                add = input(f"Enter you want to add task = ")
                tasks.append(add)
                print(f"Tasks{add} has been added successfully = ")

            elif operation == 2:
                update_val = input(f"Enter the taks you want to update = ")
                if update_val in tasks:
                    UP = input("Enter the taks you want to update = ")
                    ind = tasks.index(update_val)
                    tasks[ind] = UP
                    print(f"Enter the updated value {UP}")

            elif operation == 3:
                del_val = input(f"Enter you want to delete = ")
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task {del_val} has been deleted____") 

            elif operation == 4:
                print(f"Total tasks = {tasks}")
            elif operation == 5:
                print("Closing the program__")

                break
            else:
                print("invalid input")                           
