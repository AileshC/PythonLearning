## Create a problem with the following menu and full working code ##

```
--------- MENU ---------
: 1:   Add
: 2:   Substract
: 3:   Multiply
: 4:   Division
: 5:   Div
: 6:   Mod
: 7:   Square
: 8:   Cube
--------------------------
: 0:   Exit
--------------------------
What is your choice:

----------------------
Please enter first number:
Please enter second number:
--------------------------
The answer is: 
--------------------------
Do you want to continue(Yes) or exit(No/Exit)?
```
- Solution :
'''
 def user_menu():
    print("----Menu----")
    print("Add---do addition")
    print("Sub---do substraction")
    print("Mul---do Multiplacation")
    print("Divis---do Division")
    print("Mod---find remainder")
    print("square---square a number")
    print("cube---cube a number")
    print("0/Q---QUIT")
    user_choice = input("Please enter your menu function")
    user_number2 = 0
    if function_finder(user_choice) != 'ERROR':
        user_number1 = input("Please enter your first number")
        user_number1 = int(user_number1)
        if user_choice not in ["square", "cube"]:
            user_number2 = input("Please enter your second number")
            user_number2 = int(user_number2)
        print("you have done",function_finder(user_choice),"and your new number is",calc(user_number1,user_number2,user_choice))
    else:
        print("Wrong choice!!")
    return user_choice
    
def function_finder(math):
    
    if math == "add" or math == "Add" :
        fun = "Addition"
    elif math == "sub" or math == "Sub" :
        fun = "Substraction"
    elif math == "mul" or math == "Mul" :
        fun = "Multiplacation"
    elif math == "divis" or math == "Divis" :
        fun = "Division"
    elif math == "square" or math == "Square" :
        fun = "Squaring"
    elif math == "cube" or math == "Cube" :
        fun = "Cubing"
    elif math == "mod" or math == "Mod" :
        fun = "finding the remainder"
    else :
        fun = "ERROR"
        
    return fun
    
def calc(num1,num2,funk) :
    
    if funk == "add" or funk == "Add" :
        value = num1 + num2
    elif funk == "sub" or funk == "Sub" :
        value = num1 - num2
    elif funk == "mul" or funk == "Mul" :
        value = num1 * num2
    elif funk == "divis" or funk == "Divis" :
        value = num1 / num2
    elif funk == "Mod" or funk == "mod" :
        value = num1 % num2
    elif funk in ["square", "Square"] :
        value = num1*num1
    elif funk.upper() == "CUBE" :
        value = num1*num1*num1
    elif type(num1) == str or type(num2) == str :
        value = "ERROR"
    else :
        value = "ERROR"
        
    return value

user_choice = user_menu()
while user_choice != '0':
    user_choice = user_menu()
'''
