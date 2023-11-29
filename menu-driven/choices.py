'''WAP to calculate smaller between two numbers.
WAP to calculate greatest among any three numbers.
WAP to print the middle number among three numbers.
WAP to print the following series: 5 10 15 20 .... so on upto tenth terms.
WAP to print the odd numbers from 100 to 20
Exit
and also ask the user to continue the menu choice.'''

def smaller():
    num1=int(input("enter a number: "))
    num2=int(input("enter another number: "))
    if (num1 < num2) :
        print ("the smaller numer is", num1)
    else:
        print ("the smaller number is", num2)

def greatest():
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    num3=int(input("Enter third number: "))
    if (num1 > num2 and num1 > num3):
        print ("the greatest number is ", num1)
    elif (num2 > num1 and num2 > num3):
        print ("the greatest number is", num2)
    else:
        print ("the greatest number is ", num3)

def middle():
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    num3=int(input("Enter third number: "))
    if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
        print ("the middle number is ", num1)
    elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
        print ("the middle number is ", num2)
    else:
        print("the middle number is", num3)

def series():
    for i in range (5,55,5):
        print(i, end=",")

def odd():
    for i in range (99,20,-2):
        
        print (i, end=",")

def conti():
    a=int(input("You wanna continue: \n1.Yes \n2. No \n"))
    match (a):
        case 1:
            menu()
        case 2:
            exit()


def menu():
    n=int(input("enter your choice: \n1.calculate smaller between two numbers\n2. calculate greatest among any three numbers.\n3.print the middle number among three numbers\n4.print the following series: 5 10 15 20 .... so on upto tenth terms.\n5.print the odd numbers from 100 to 20. \n your choice: "))
    match(n):
        case 1:
            smaller()
            conti()
        case 2:
            greatest()
            conti()
        case 3:
            middle ()
            conti()
        case 4:
            series ()
            conti()
        case 5:
            odd ()
            conti()
        case 6:
            exit()
        case _:
            invalid input
    
menu ()
