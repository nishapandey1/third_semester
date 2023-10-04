'''WAP to doa menu driven progrm
1. Addition
2.subtraction
3.division
4.multiplication'''

# num1=int(input("enter a number: "))
# num2=int(input("enter another number: "))


# a=int(input("your option:\n 1.Addition \n 2.subtraction \n 3.division \n 4.multiplication \n choose your option: "))

# match a:
#     case 1:
#         print ("Addition", num1 + num2 )
#     case 2:
#         print ("subtraction", num1 - num2 )
#     case 3:
#         print ("division", num1 / num2 )
#     case 4:
#         print ("multiplication", num1 * num2 )
#     case 5:
#         print ("invalid input")

num1=int (input("enter a number: "))
num2=int(input("enter another number: "))
def add (num1, num2):
    print("addition", num1 + num2 )
def sub (num1, num2):
    print("subtraction", num1 - num2)
def div (num1, num2):
    print("division", num1 / num2 )
def multi (num1, num2):
    print("multiplication", num1 * num2)

n=int(input("enter your choice: "))
match(n):
    case 1:
        add( num1, num2 )
    case 2:
        sub( num1, num2 )
    case 3:
        div( num1, num2 )
    case 4:
        multi( num1, num2 )
