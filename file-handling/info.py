'''1)WAP to enter your name, address, gender, age,faculty and roll number into a filename "info.txt".
    2) WAP to display name,address and faculty from the file "info.txt".'''

name=input("enter your name: ")
address=input("address: ")
gender=input("gender:")
age=input("age: ")
faculty=input("faculty: ")
roll_number=int(input("roll_number: "))

f=open("info.txt","w")

f.write("Name= Nisha")
f.write("\naddress= Kalanki")
f.write("\ngender=female")
f.write("\nage=19")
f.write("\nfaculty= Ethical")
f.write("\nroll number=23")
f.close()

f=open("info.txt","r")

lines=f.readlines()
print(lines[0])
print(lines[1])
print(lines[4])

f.close()
