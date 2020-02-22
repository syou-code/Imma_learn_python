cool_name = 'sAiLuN'
# Remember that strings are immutable.

print('my name is ', cool_name)
print('my data type is ', type(cool_name))

# i want to downcase it
print('downcase', cool_name.lower())

# i want to upcase it
print('upcase', cool_name.upper())

#  want to loop through your name
# in python, you can see a string a list of characters.
# meaning you can loop through each character and print it out.
print('here i print out each char')
for _char in cool_name:
    print(_char)

# i want to print out 3rd char in cool_name
print('here is my 3rd character:', cool_name[2])


# i can join an array of characters into a string.
arry = ['i','m','pretty','cool']
print('@'.join(arry))
