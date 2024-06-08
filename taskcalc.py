from tkinter import *

# add function
def add(n1,n2):
    return n1+n2
   
# subtract function
def subtract(n1,n2):
    return n1-n2
   
# Multiply function
def multiply(n1,n2):
    return n1*n2
   
# Divide function
def divide(n1,n2):
    return n1/n2
while True:
    print("\n Welcome to Calculator")
    print("Please select from the following operations : \n"
            "1. Add \n"
            "2. Subtract \n"
            "3. Multiply \n"
            "4. Divide \n"
            "5. Quit")
           
    # Taking operator input from the user

    operator = int(input("Select operations from 1,2,3,4,5 : "))
   
    # Taking two numbers from user
    if(operator==5):
        print("You have succesfully quit the programe")
        break
    else:
        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))
       
        if(operator==1):
            # print(f"Addition of {num_1} and {num_2} is {add(num_1,num_2)}")
            root = Tk() 
            root.geometry("300x200")    
            msg = Message( root, text = f"Addition of {num_1} and {num_2} is {add(num_1,num_2)}")
            msg.pack()     
            root.mainloop()  

        elif(operator==2):
            # print(f"Subtraction of {num_1} and {num_2} is {subtract(num_1,num_2)}")
            root = Tk() 
            root.geometry("300x200")    
            msg = Message( root, text =f"Subtraction of {num_1} and {num_2} is {subtract(num_1,num_2)}" )
            msg.pack()     
            root.mainloop() 

        elif(operator==3):
            # print(f"Multiplication of {num_1} and {num_2} is {multiply(num_1,num_2)}")
            root = Tk() 
            root.geometry("300x200")    
            msg = Message( root, text = f"Multiplication of {num_1} and {num_2} is {multiply(num_1,num_2)}")
            msg.pack()     
            root.mainloop() 
        elif(operator==4):
            # print(f"Division of {num_1} and {num_2} is {divide(num_1,num_2)}")
            root = Tk() 
            root.geometry("300x200")    
            msg = Message( root, text = f"Division of {num_1} and {num_2} is {divide(num_1,num_2)}")
            msg.pack()     
            root.mainloop() 

