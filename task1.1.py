#1. The Calculator App
#Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
print("Hello, Welcome to your Calculator")
while True:

    operation = input("First enter the calculation you would like to perform: add,subtract,multiply, or divide: ")
    first_num = int(input("Enter the first number: "))
    second_num = int(input("enter second number: "))
    add_num = (first_num + second_num)
    subtract_num = (first_num - second_num) 
    multiply_num = (first_num * second_num)
    try:
        divide_num = (first_num / second_num)
    except ZeroDivisionError:
        print("Can't divide by 0")
    if (operation) == "add":
        print (f"{first_num} + {second_num} = {add_num}")
    elif (operation) == "subtract":
        print (f"{first_num} - {second_num} = {subtract_num}")
    elif (operation) == "multiply":
        print (f"{first_num} * {second_num} = {multiply_num}")
    elif (operation) == "divide":
        print (f"Please enter a valid operation")
          
        
    
        

    
    
    
        