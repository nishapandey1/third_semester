'''WAP to print the fibonacci series upto 10th terms.'''

num1=1
num2=1
print(num1,num2,end=" ")
for i in range (10):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3, end=" ")