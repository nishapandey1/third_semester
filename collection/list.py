# list=["hello", "hi","bye","welcome"]
# print (list)
# print (type(list))
# print(list[0])
# print(list[1])
# print(list[-1])

# '''WAP a program to print the list with diffferent printing methods using list indexing'''
# a=input("enter your input.")
# print (a)

# movies=["superman", "flash","Talk to me","krish","abhijeet","minions", "bao"]
# print (type(movies))
# print (movies[3:5])
# print (movies[3:])
# print (movies[:2])
# print(movies[-4:-1])
# movies.insert(2,"your name")
# movies.append("paperman")
# movies.pop(4)
# movies.remove("flash")
# movies.sort()
# movies[1]="silent voice"
# movies[2:4]=["forest flis","my name"]
# movies.sort(key=str.lower)
# print (movies)

# '''concatenation'''
# list1=["doremon","novita","krish"]
# list2=["apple","mango","Banana","grapes"]
# list3=list1+list2
# print(list3)

# fruits=["apple","mango","banana","grapes"]
# fruits.sort(reverse=True)
# print(fruits)

# list1=["doremon","novita","krish"]
# list2=["apple","mango","Banana","grapes"]
# list1.extend(list2)
# print(list1)

# list1=["doremon","novita","krish"]
# list3=list1.copy()
# print(list3)

# list1=["doremon","novita","krish"]
# list2=["apple","mango","Banana","grapes"]
# list1.extend(list2)
# print(list1)

list1=["doremon","novita","krish"]
list2=[1,2,3,4,10,100,8]
for i in list2:
    list1.append(i)
print(list1)
