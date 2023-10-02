name=input("enter your name: ")
std_id=int(input("enter your student id: "))
faculty= input ("enter the faculty: ")

english=int (input("enter your english marks: "))
maths=int (input("enter your maths marks: "))
science= int (input("enter your science marks: "))
nepali= int (input("enter your nepali marks: "))
social= int (input("enter your social marks: "))
marks=(english + maths + science + nepali + social )
result= (marks/500)*100
if ( english < 40 or maths < 40 or science < 40 or nepali < 40 or social < 40):
    print ("fail")
elif ( result > 70 ):
    print ("you passed in Distinction")
elif ( result >= 60 and result < 70):
    print ("you passed in first division")
elif ( result >= 50 and result < 60):
    print ("you passed in second division") 
elif ( result >= 40 and result < 50):
    print ("you passed in third division")
else:
    print ("you failed!")
       