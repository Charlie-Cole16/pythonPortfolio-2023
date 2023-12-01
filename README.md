# Python Projects

Welcome to my portfolio, this will look at the python projects I have created this year:

## Mastemind
Code from mastermind:
```python
'''
Program: Mastermind Code
Version: 1.0
'''
import random

### FUNCTIONS/PROCEDURES AREA ###
def viewRule():
    print("The rules of the game are as follows: ")

def machineNumberGenerate():
    # Will generate a random 4 digit number:
    iNum = random.randrange(1000, 10000)
    return iNum

def userGuessNumber():
    # Ask the user to enter in a random number (integer value)
    iNum = int(input("Enter in a 4 digit number that you would like to guess: "))
    return iNum

def checkGuess(iMachine, iUser):
    if iMachine == iUser:
        print("You have the correct answer, well done!")
    else:
        iAttempt = 1
        iCorrectPosition = 0
        iWrongPosition = 0
    # Write a while loop which runs if the machine and user numbers do not match:
    while(iMachine != iUser):
        # In order to allow us to split out a number into seperate chunks, we will need to change into a string then convert back:
        iMachineString = str(iMachine)
        iUserString = str(iUser)

        for iCount in range(0,4):
            if(iMachineString[iCount] == iUserString[iCount]):
                iCorrectPosition += 1
            elif(iMachineString[iCount] in iUserString):
                iWrongPosition += 1

        print(f"Youu did not get the correct set of numbers, but there are {iCorrectPosition} in the correct position")
        print(f"You did not have the following correct numbers in the wrong position {iWrongPosition}")
        input()
        # Your turn - the above provides only whether the number is in the correct position; using this knowlage to help support, we want to check through all of the numbers to check how many numbers are correct but are in the wrong position
 


### MAIN AREA ###
print("Welcome to the mastermind program, rules for the game")

# Function to explain the rules of the game:
iRulesInput = int(input("Do you want to veiw the rules of the game, choose 1 if you do, choose 0 if you dont: "))

if iRulesInput == 1:
    viewRule()

iMachineNumber = machineNumberGenerate()
iUserGuess = userGuessNumber()
checkGuess(iMachineNumber, iUserGuess)
```

### Output
![alt tag for screen readers](images/MastermindScreenShot1.png)
![alt tag for screen readers](images/MastermindScreenShot2.png)

## Calculator
Code from Calculator
```python
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
```

### Output
![alt tag for screen readers](images/CalculatorScreenShot1.png)
![alt tag for screen readers](images/CalculatorScreenShot2.png)
