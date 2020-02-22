# integers: 0, 1, 2 3... -1, -2, ...

a = 1

print('imma number int:', a)
print('my type is:', type(a))

print('i love adding', 1 + 2)

a = 1
b = 1.0

# so think of float as the dominate one. 
# when you add, subtract, multiply, divide with a float, it becomes a float.
print('what is my type?', type(a + b))
print('because imm actually', a + b)

# i loop through [0, 5) increment of 1
print('loop')
for i in range(0, 5, 2):
    print(i)


# in python.. there isn't actually a limit to int.
t = 99999999999999999999999999999999999999999999999999999999999999999999999999999
print('im big', t + 1)


# i want to convert int to a float
b = float(a)
print('im a float now', b)
print('type', type(b))