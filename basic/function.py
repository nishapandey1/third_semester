#WAP to print the multiplication table of 5
#WAP to print the multiplication from 1 to 10 upto 10 multiples
#WAP to find the factorial of given number
#WAP to check whether the entered value is palindrome or not.

def multi_five():
    for i in range(1,11,1):
        print(f"5 * {i} = {5*i}")

def multi_ten():
    for i in range(1,11,1):
        for j in range(1,11,1):
            print(f"{i} * {j} = {i*j}")

def factorial():
    num=int(input("Please enter a number: "))
    factorial=1
    for i in range(num,1,-1):
        factorial=factorial*i
    print(f"The factorial of the given number {num} is {factorial}.")

def palindrome():
    thing=input("Please enter the string or number: ")
    rev_thing=thing[::-1]
    if thing==rev_thing:
        print(f"The given number/string {thing} is a palindrome.")
    else:
        print(f"The given number/string {thing} is not a palindrome.")

def cont():
    print("Do you want to continue?\n1. Yes\n2. No")
    choice=int(input("Choice: "))
    match choice:
        case 1:
            menu()
        case 2:
            print("Exiting....")
            exit()


def menu():
    print("Please select a choice: ")
    print("1. Print the multiplication table of 5.\n2. Prin the multiplication from 1 to 10.\n3. The factorial of given number.\n4. Check if given number or string is palindrome.")
    choice = int(input("Choice: "))
    match choice:
        case 1:
            multi_five()
            cont()
        case 2:
            multi_ten()
            cont()
        case 3:
            factorial()
            cont()
        case 4:
            palindrome()
            cont()
        case _:
            print("Wrong choice.")
            cont()

menu()
 