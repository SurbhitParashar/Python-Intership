from tkinter import *
print("********************************************************\n"
    "Welcome to Phone Book Directory! \n"
      "********************************************************")

all_contact=[]

def addcontact():
    # taking contact info from user
    name = input("enter your name : ")
    phone_no = input("enter your phone number : ")
    email = input("enter your email id : ")
    address = input("enter your address : ") 

    # putting all information in list
    l1=[name,phone_no,email,address]

    #putting all l1 list in one list for more organised information 
    all_contact.append(l1)
    
    # writing list in a diffrent text file
    # file1=open("data.txt","w")
    # file1.writelines(l1)
    # file1.close()

    print("\n Your contact has been saved successfully! \n")

def display_contact():
    #this will print a 2d list in which our phone directory exist
    print("\n Here is a list of saved contact : \n")

    #first it will check whether list is empty or not
    if len(all_contact)==0:
        print("List is Emplty : []")
    #otherwise print the all contact list data 
    else:
        print(all_contact)

        root = Tk() 
        root.geometry("300x200")    
        msg = Message( root, text = f"List of all contact are :\n {all_contact}")
        msg.pack()     
        root.mainloop()

def search_contact():
    print("Enter choice from : \n"
                       "1. Name\n"
                       "2. Phone number \n")
    Choice = int(input("enter from the above option : "))
    
    #creating an empty list where we can append our specific search contact
    temp_l1=[]

    if(Choice==1):
        name = str(input("enter the name : "))

        for i in range(len(all_contact)):
            if name== all_contact[i][0]:
                temp_l1.append(all_contact[i])
    
    elif(Choice==2):
        no = int(input("enter the phone no.: "))

        for i in range(len(all_contact)):
            if no == all_contact[i][1]:
                temp_l1.append(all_contact[i])

    else:
        print("please enter the correct input")

    print(temp_l1)

    root = Tk() 
    root.geometry("300x200")    
    msg = Message( root, text = f"Here is your searched contact : \n {temp_l1}")
    msg.pack()     
    root.mainloop()


def Update_contact():
    print("For update contact choose one from following :\n"
          " 1. Name \n 2. phone no. \n 3. email \n 4. address \n")
    option = int(input("enter your choice from obove : "))

    name = str(input("enter name of person to change its detail : "))

    if option==1:
        for i in range(len(all_contact)):
            if name==all_contact[i][0]:
                new_name=str(input("enter new name : "))
                all_contact[i][0]=new_name
    
    elif option==2:
        for i in range(len(all_contact)):
            if name==all_contact[i][0]:
                new_no=int(input("enter new no.: "))
                all_contact[i][1]=new_no

    elif option==3:
        for i in range(len(all_contact)):
            if name==all_contact[i][0]:
                new_email=str(input("enter new email : "))
                all_contact[i][1]=new_email

    elif option==4:
        for i in range(len(all_contact)):
            if name==all_contact[i][0]:
                new_address=input("enter new address : ")
                all_contact[i][1]=new_address

    print("Your phone directory updated succesfully! \n ")

def delete_contact():
    del_name = input("enter name of the person to delete it's contact : ")
    for i in range(len(all_contact)):
        if del_name==all_contact[i][0]:
            all_contact.remove(all_contact[i])
    print("Contact has been deleted successfully \n")


def del_all_contact():
    all_contact.clear()
    print("All contact has been removed \n ")


while True:
 
    print("Press the following key for further action : \n"
        "1. Add Contact \n"
        "2. Display Contact \n"
        "3. Search Contact \n"
        "4. Update Contact \n"
        "5. Delete a Contact \n"
        "6. Delete whole phone book directory \n"
        "7. Quit\n")

    # Taking operator input from the user

    action = int(input("Select operations from 1,2,3,4,5,6,7 : "))
   
    # Taking two numbers from user
    if(action==7):
        print("*************************************** \n"
              "Thanks for using phone book \n"
            "You have succesfully quit the Phone Book! "
            "*****************************************")
        break

    else:
        if(action==1):
            addcontact()
            
        elif(action==2):
            display_contact()

        elif(action==3):
            search_contact()

        elif(action==4):
            Update_contact()

        elif(action==5):
            delete_contact()
        
        elif(action==6):
            del_all_contact()
        
        else:
            print("please try to enter a correct number!")