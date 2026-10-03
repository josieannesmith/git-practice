import json
tasks = []
json_tasks = []
with open("/Users/josephinesmith/Documents/Python/git-practice/tasks","r") as file:
    json_tasks = json.load(file)
tasks = json_tasks

def main_menu():
    print("\nTASKS \n1. Add task \n2. View tasks \n3. Complete task \n4. Delete task \n5. Quit")
    try:
        menu = int(input("Choose an option from the menu: "))
    except:
        if menu > 5 or menu < 1:
            print("Error. Please enter a number between 1-5")
        main_menu()


    if menu == 1:
        add_task()
    elif menu == 2:
        view_tasks()
    elif menu == 3:
        complete_task()
    elif menu == 4:
        delete_task()

def task_list():
    for number, task in enumerate(tasks, start = 1):                #shows the tasks that are saved. number=index, task = dictionary
        print(number,".", task["task"], task["complete"])


def add_task():  
    new_task = input("Enter new task: ")
    tasks.append({"task" : new_task, "complete" : " - Not done"})
    with open("/Users/josephinesmith/Documents/Python/git-practice/tasks","w") as file:
        json.dump(tasks,file)
    main_menu()

        
def view_tasks():
    task_list()
    main_menu()

def complete_task():
    task_list()
    completed_task = int(input("\nWhich number task has been complete? "))-1
    tasks[completed_task]["complete"] = " - Done"
    with open("/Users/josephinesmith/Documents/Python/git-practice/tasks","w") as file:
        json.dump(tasks,file)
    main_menu()

def delete_task():
    task_list()
    delete_task = int(input("\nWhich number task would you like to delete? "))-1
    del tasks[delete_task]
    with open("/Users/josephinesmith/Documents/Python/git-practice/tasks","w") as file:
        json.dump(tasks,file)
    main_menu()

main_menu()



