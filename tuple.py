my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  
# modifying elements
#my_tuple.append (9)(/immutable/)

# list with in the tuple
my_tuple2 =([1,2,3],5,6,7)
print(my_tuple2)
my_tuple2[0].append(4)
print(my_tuple2)
# Iterating through a tuple
for item in my_tuple:
    print(item)