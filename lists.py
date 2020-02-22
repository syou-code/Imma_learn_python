# array is called list in python
# order matters a lot to me.
# i can have duplicate values
arry = [1,1,2,3,4,5,'a','b','c']
print('im an array', arry)

# i can loop through an array.
# let's do for each loop.
for item in arry:
    print('item', item)

print()
print()

# i can loop through an array using range
for i in range(0, len(arry), 1):
    print('position', i)
    print('item', arry[i]) # here i'm calling the array with the position.


# i can add arrays together

a = [7,8,9,1,1,2,3]
b = [4,5,6]

print('combined array', a + b)
print('combined array differently', b + a)


# i can add element to current list
a.append(11)

print('i just added a value', a)

# i can also sort my array
print('sorted', sorted(a))