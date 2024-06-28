#The Shopping List Maker
#Objective: The aim of this assignment is to create a program that helps users make a shopping list.
#Task 1: Write a function that lets the user add items to a list.
#Task 2: Include a function to remove items from the list.
#Task 3: Add a function that prints out the entire list in a formatted way.

list = []
while True:
    shopping_list = input("To add or remove items from your shopping list type 'add' or 'remove' if done type 'done' ")
    if shopping_list == ('add'): 
        new_list=input("What item would you like to add? ")
        list.append(new_list)
        print(f"{new_list} has been added to your shopping list")
        print(f"Your updated shopping list is: {list}")
    elif shopping_list == ('remove'):
        remove_list = input("What item would you like to remove from your shopping list? ")
        if remove_list in list:
            list.remove(remove_list)
        print(f"{remove_list} has been removed from your shopping list")
        print(f"Your updated shopping list is: {list}")
    elif shopping_list == ('done'):
        print(f"Your shopping list is done. Your updated list is: ") 
        print(f"{list}")
        break
    
        
    
        
      
                       
                    