'''Perform following functions in collections'''
'''printing the collection'''
'''printing range selection along with negative indexing'''
'''length and type checking'''
'''counting same values'''
'''insert'''
'''delete'''
'''sorting (ascending and descending)'''
'''reverse'''
'''extending or joining'''
'''allow duplicates or not'''

#list
'''printing the collection'''
# list=["Hello","Ina","1"]
# print(list)
# print(type(list))

'''printing range selection along with negative indexing'''
# list=["Hello","Ina","1"]
# print(list[-2])

'''length and type checking '''
# list=["Hello","Ina","1"]
# print(list)
# print(len(list))
# print(type(list))

'''counting same values'''
# list=["Hello","Ina","Hello"]
# print(list.count("Hello"))


'''insert'''
# list=["ehatt","pilots","ned","mendes",21]
# list.insert(1,"miquel")
# print(list)

'''delete'''
# list=["ehatt","pilots","ned","mendes",21,"supp"]
# list.delete(-1) (no delete attribute)
# print(list)

'''sorting (ascending and descending)'''
# list=["ehatt","pilots","ned","mendes","supp"]
# list.sort()
# list.sort(reverse=True)
# print(list)

'''reverse'''
# list=["ehatt","pilots","ned","mendes","supp"]
# list.reverse
# print(list)

'''extending or joining'''
# list1=["ehatt","pilots","ned","mendes","supp"]
# list2=["Hello","Ina",1]
# list1.extend(list2) 
# print(list1)

'''allow duplicates or not'''
# list1=["ehatt","pilots","ned","mendes","supp"]
# list2=["Hello","Ina",1]
# duplicated_list1 = list1[:]
# duplicated_list2 = list2[:]
# print("Duplicated list 1:", duplicated_list1)
# print("Duplicated list 2:", duplicated_list2)


# #tuple
'''printing the collection'''
# tuple=(1,"hi","new world")
# print(tuple)

'''printing range selection along with negative indexing'''
# tuple=(1,"hi","new world")
# print(tuple[-2])

'''length and type checking '''
# tuple=("Hello","Ina",1)
# print(tuple)
# print(len(tuple))
# print(type(tuple))

'''counting same values'''
# tuple=("Hello","Ina","Hello")
# print(tuple.count("Hello"))

'''insert'''
# tuple=("ehatt","pilots","ned","mendes",21)
# tuple.insert(1,"miquel")
# print(tuple) (no insert attribute)

'''delete'''
# tuple=("ehatt","pilots","ned","mendes",21,"supp")
# tuple.delete(-1) (no delete attribute)
# print(tuple)

'''sorting (ascending and descending)'''
# tuple=("ehatt","pilots","ned","mendes","supp")
# tuple.sort()
# tuple.sort(reverse=True)
# print(tuple) (no sort attribute)

'''reverse'''
# tuple=("ehatt","pilots","ned","mendes","supp")
# tuple.reverse
# print(tuple) (no reverse attribute)

'''extending or joining'''
# tuple1=("ehatt","pilots","ned","mendes","supp")
# tuple2=("Hello","Ina",1)
# tuple1.extend(tuple2) 
# print(tuple1) (no extend attribute)

'''allow duplicates or not'''
# tuple1=("ehatt","pilots","ned","mendes","supp")
# tuple2=("Hello","Ina",1)
# duplicated_tuple1 = tuple1[:]
# duplicated_tuple2 = tuple2[:]
# print("Duplicated tuple1:", duplicated_tuple1)
# print("Duplicated tuple2:", duplicated_tuple2)
