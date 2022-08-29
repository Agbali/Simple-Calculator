#Creating a CLI Calculator
#Define the addition function that adds two numbers

def addition(x,y):
    return x + y
#Define the subtraction function that subtracts two numbers
def subtraction(x,y):
    return x - y
#Define the multiplication function that multiplies two numbers
def multiply(x,y):
    return x * y
#Define the division function that dividies two numbers
def divide(x,y):
    return x / y

#Define the modulus operandi 
def modulus(x,y):
    return x % y

#Printing instructions on the calculator
print("Calculator")
print("------- Instructions -------")
print(" 1 for Addition \n 2 for Subtraction \n 3 for Multiplication \n 4 for Division \n 5 for modulus operations")

while True:

    #Take input from user

    operations = input(" Type '1' '2' '3'  '4' '5': ")

    #Check if the number they selected is among the available options

    if operations in ('1','2','3','4', '5'):
        numb1 = float(input("Enter first number: "))
        numb2 = float(input("Enter second number: "))

        if operations == '1':
            print(numb1, "+", numb2,"=", addition(numb1, numb2))
        
        elif operations == '2':
            print(numb1, "-", numb2, "=", subtraction(numb1, numb2))
        
        elif operations == '3':
            print(numb1, "*", numb2, "=", multiply(numb1, numb2))
        
        elif operations == '4':
            print(numb1, "/", numb2, "=", divide(numb1, numb2))
        
        elif operations == '5':
            print(numb1, "%", numb2, "=", modulus(numb1, numb2))

        #Check if user wishes to calculate again
        #Else break the loop if the answer is no

        calculate_again = input("Do you want to calculate again? (yes/no): ")

        if calculate_again == "no":
            break

    else:
        print ("Invalid input")