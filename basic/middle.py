num1=int(input("enter first number ")) 
num2=int(input("enter second number ")) 
num3=int(input("enter third number ")) 

if (num1 > num2 and num1 < num3) or (num1 > num3 and num1 < num2):
    print ("the middle number is", num1)
elif(num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    print ("the middle number is", num2)
elif (num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2):
    print ("the middle number is", num3)
else:
    print ("enter different number")
