print("############################################\n"
      "Welcome to the To-Do List!!! \n"
      "############################################")

#here is an empty list to store the to do task 
#dictionary is used to store the data number wise in more organised way
to_do={}

#here is a programe to add initial task for the current day or the upcoming day
#it is made with the purpose so that user can make a comprihensive list for it's task
def initial_task_add():
    no=int(input("enter number of task to add : "))
    for i in range(no):
        key=i
        desp_i=input(f"enter the description of the task {i+1} : ")
        to_do[key+1]=desp_i
        print("\n Task added successfully! \n")
        

#it provide user a menu to choose different option for further edit it's to do list
def menu():
    print("Choose from the following operations to perform \n"
      "1. Add Task \n"
      "2. View Task \n"
      "3. Mark as Done \n"
      "4. Remove To-Do list\n"
      "5. Remove a Task\n"
      "6. Exit \n")
    
#function is made to add task at later stage if user forget at initial to add at to do list
def add_task():
    key=len(to_do)
    # print(key)
    desp = input(f"enter the description of the task {key+1} : ")

    #here we are making a new key value pair in our dictionary to add more task later
    to_do[key+1]=desp    
    print("Task added succesfully!")
    

def view_task():
    print(to_do)

#here we are asking user for the complition of the task 
#user can remove done task from the to do list 
def mark_done():
    print("enter the number of task or description of task : \n"
                      "1. Task number \n"
                      "2. Task description \n")
    task_done=int(input("enter operation from the following : "))
                      
    #if task number is input then it will first check number then mark its done
    if task_done==1:
        # print(1)
        task_num=int(input("enter the task number : "))
        for i in range(len(to_do)):
            # print(2)
           
            temp_desp=to_do.get(i+1)
            key_list = list(to_do.keys())
            val_list = list(to_do.values())

            position = val_list.index(temp_desp)
            a=key_list[position]

            # print(a)
            if a==task_num:

                to_do[i+1]=(f"{temp_desp} ✔")
                print("Completed task has been marked done!")

    #if task description is input then it will first check its description then mark its done
    elif task_done==2:
        task_des = input("enter the description of task : ")
        for i in range(len(to_do)):
            temp_desp=to_do.get(i+1)
            if temp_desp==task_des:
                to_do[i+1]=(f"{temp_desp} ✔")
                print("Completed task has been marked done!")
            
    else:
        print("please enter a correct input")

    

def remove_to_do():
    to_do.clear()

def remove_a_to_do():
    print("enter the number of task or description of task : \n"
                      "1. Task number \n"
                      "2. Task description \n")
    task_done=int(input("enter operation from the following : "))
                      
    #if task number is input then it will first check number then remove it 
    if task_done==1:
        # print(1)
        task_num=int(input("enter the task number : "))
        for i in range(len(to_do)):
            # print(2)
           
            temp_desp=to_do.get(i+1)
            key_list = list(to_do.keys())
            val_list = list(to_do.values())

            position = val_list.index(temp_desp)
            a=key_list[position]

            # print(a)
            if a==task_num:

                to_do.pop(i+1)
                print("Task has been removed!")

    #if task description is input then it will first check its description then mark its done
    elif task_done==2:
        task_des = input("enter the description of task : ")
        for i in range(len(to_do)):
            temp_desp=to_do.get(i+1)
            if temp_desp==task_des:
                to_do.pop(i+1)
                print("Task has been removed!")
            
    else:
        print("please enter a correct input")

initial_task_add()

while True:
    
    menu()
    action = int(input("Enter the operation from the following : "))
    
    if action==1:
        add_task()
    elif action==2:
        view_task()
    elif action==3:
        mark_done()
    elif action==4:
        remove_to_do()
    elif  action==5:
        remove_a_to_do()
    elif action==6:
        print("################################################### \n"
          "you have succesfully exit the programe \n"
          "###################################################")
        break

