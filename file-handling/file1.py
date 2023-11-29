# file pointer = open (filename with extension,file opening modes)
# f=open (file.txt)

# f=open("d:\semester 3\programming 2\hello.txt","r")
# print(f.read())


# f=open("file.txt","x")
# f.write("heloo")
# f.close()

# f=open("file.txt", "w")
# f.write("hello")

# f=open("file.txt","w")
# f.write ("hii")
# f.write("\n")
# f.write("Byee")
# f.close()

f=open("file.txt","a")
f.write("\n")
f.write("what's up bro!?")
f.close()