# a dictionary is similar to a set, but it's key value
# a set i just all keys.
# dictionary is a key-value pairs.

# {<key>: <value>}
d = {'name': 'Sailun', 'dob': '08141989'}

print('dictionary', d)

# you can only have 1 unique key. BUT you can have duplicate values

name = {'first_name': 'Nguyen', 'last_name': 'Nguyen'}

print('first and last name', name)

# i can change the vaue of the key
name['first_name'] = 'Sailun'
name['last_name'] = 'You'

print('my new name', name)

# but what happens if i don't have a key doesn't exist
# it will add middle_name key to the name dictionary
name['middle_name'] = 'cool'

print('my new name', name)


print('my first name is', name['first_name'])
print('my last name is', name['last_name'])

# second_middle_name is not defined. that's why it errors out.
print('my second middle name', name['second_middle_name'])