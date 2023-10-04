'''Write a menu driven program for the following cases:
1. Hello
2.Hi
3.Bye
4.Welcome
5. Exit'''

# a=int(input("your option:"))
# match a:
#     case 1:
#         print("hello")
#     case 2:
#         print("Hi")
#     case 3:
#         print("Bye")
#     case 4 | 6 | 7 | 8 :
#         print("Welcome")
#     case 5:
#         (exit)

def info():
    print("hello")
def bye():
    print("Bye")
def hi():
    print ("hello")

n=int(input("enter your choice: "))
match(n):
    case 1:
        info()
    case 2:
        bye()
    case 3:
        hi()

        
