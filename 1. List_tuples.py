# Update Python interpreter
# Go to Python preferences -> Projects -> Project Folder -> Python interpreter

# Run - Either select the file name or select the Current File. Python is case sensitive.

x = 152 + 100
# this is variable x
print(x)

# Python has packages defined, and we can import them to used function from packages.
from math import sqrt

x = 4
print(sqrt(x))

my_list1 = [1, 22, 3, 4, 5, 6, 11]  # it's a list
my_list2 = list(range(1, 7))  # creating list from range of numbers 1 to 7 (goes to 7-1)
my_list3 = list(range(1, 50, 5))  # list begin from 1, increment by 5 until it gets near to 50
print(my_list1)
print(my_list2)
print(my_list3)
print(my_list1[2])  # position starts from 0 then 1 then 2 so on
print(my_list1[-2])  # last two positions, here it starts with 1 as -0 means nothing.
print(my_list1[2:6])  # print from 3rd(0,1,2 which is 3) to (7-1).
print(len(my_list1))
print(max(my_list1))
my_list1[0] = 122.  #updates the value at 0 position
print(my_list1)

#  add an element to my_list1
my_list1.append(88)
print(my_list1)

#  reverse list
my_list1.reverse()
print(my_list1)

#  add two list together
print(my_list1 + my_list2)

# max number in the list
number = [11, 23, 34, 8, 89, 90]
max_number = number[0]
for values in number:
    if values > max_number:
        max_number = values
print(max_number)

# remove duplicate from list
matrix = [11, 11, 23, 24, 23, 26, 27, 28]
unique_matrix = []
for values in matrix:
    if values not in unique_matrix:
        unique_matrix.append(values)
print(unique_matrix)

# Tuples
city = "Pune"
print(type(city))
<class 'str'>

city = "Pune",   # with a comma it becomes tuple, else its a vairable for string class
print(type(city))
<class 'tuple'>

city1 = ('A', 'B', 'C')
city2 = ('1', '2', '3')
nested = (city1, city2)  # contains 2 tuples
print(nested)
print(city1[-1])
print(city1[0])

# Repetition
rep = ("Python",)*5  # repeats value 5 times inside the tuple
print(rep)
print(rep*2)  # prints 10 times, but does not modify tuple

# Slicing
print(city1)
print(city1[1:2])

#Converting list to tuple
my_list1 = [1, 22, 3, 4, 5, 6, 11]  # it's a list
print(type(my_list1))
tuple1= tuple(my_list1) 
my_list1 = tuple1      # We can convert list to tuple when we dont want list to be modifed anymore
print(type(my_list1))

#Nesting tuples in list
my_list1 = [(1, 2, 3), (4, 5, 6)]
print(my_list1)
# if we create tuple inside list then we can update those.
my_list1.append("Tuple")
my_list1.append(("Tuple", "inside", "list"))
print(my_list1)
my_list1.remove("Tuple")
print(my_list1)
my_list1.remove((1, 2, 3))
print(my_list1)

#Nesting list int the tuple
tuple1 = (['a', 'b', 'c'],['d', 'e', 'f'])
print(tuple1)
# we cant modify tuple, like add more list
# but we can modify list inside a tuple
tuple1[0].append('z')
print(tuple1)
tuple1[1].remove('d')
print(tuple1)

# Merge two tuples
tuple3=tuple1+(1,)
print(tuple3)

# Unpacking tuples
city1 = ('A', 'B', 'C')
x, y, z = city1     # need to give exact numer of vairables as in tuple
city1 = ['A', 'B', 'C']
x, y, z = city1

