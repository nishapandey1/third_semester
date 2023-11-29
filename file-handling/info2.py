''' WAP to enter your name, address, gender, age,faculty and roll number of 3 students into a file 
and display all records from the file.'''

for i in range(3):
    print(f"enter details of students:")
    name=input("\nenter your name: ")
    address=input("\naddress: ")
    gender=input("\ngender:")
    age=input("\nage: ")
    faculty=input("\nfaculty: ")
    roll_number=int(input("\nroll_number: "))

    f=open("details.txt","a")
    
    f.write(f"\nName:{name}")
    f.write(f"\nAddress: {address}")
    f.write (f"\ngender: {gender}")
    f.write (f"\nage:{age}")
    f.write(f"\nfaculty:{faculty}")
    f.write(f"\nroll_number: {roll_number}")
f=open("details.txt","r")
print(f.read())
f.close()