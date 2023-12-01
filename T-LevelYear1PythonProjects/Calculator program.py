def menu() :
    option = str(input("""welcome to the calculator
    1. Addition
    2. Subrtacion
    3. Division
    4. Multiplication
    5. Exit
    Input an option you would like to select: """))
    if option == "1":
        addition()
    elif option == "2":
        subtraction()
    elif option == "3":
        division()
    elif option == "4":
        multiplication()
    elif option == "5":
        exit
    else:
        print("Input was invalid")
        menu()

def addition():
    First_Number = int(input("Enter your first number: "))
    Second_Number = int(input("Enter your second number: "))
    Result = First_Number + Second_Number
    print(Result)
    menu()

def subtraction():
    First_Number = int(input("Enter your first number: "))
    Second_Number = int(input("Enter your second number: "))
    Result = First_Number - Second_Number
    print(Result)
    menu()

def division():
    First_Number = int(input("Enter your first number: "))
    Second_Number = int(input("Enter your second number: "))
    Result = First_Number / Second_Number
    print(Result)
    menu()

def multiplication():
    First_Number = int(input("Enter your first number: "))
    Second_Number = int(input("Enter your second number: "))
    Result = First_Number * Second_Number
    print(Result)
    menu()

menu()