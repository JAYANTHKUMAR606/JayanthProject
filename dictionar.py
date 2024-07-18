my_dict = {
    'name': 'kumar',
    'age': 21,
    'city': 'hyderabad'
}

# Accessing elements
print(my_dict['name'])  

# Modifying elements
my_dict['age'] = 26
print(my_dict)  

# Adding elements
my_dict['email'] = 'kumar@example.com'
print(my_dict)  

# Removing elements
del my_dict['city']
print(my_dict)  

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")