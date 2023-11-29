'''WAP to print the armstorng number'''
num=int(input("enter a number: "))
a=num
r=0
sum=0
while (a!=0):
    r=a%10
    sum=sum+r**3
    a=a//10

if (num==sum):
    print("It is Armstrong number")
else:
    print("It's not a armstrong.")