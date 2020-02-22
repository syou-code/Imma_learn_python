# sets are similar as lists in python
# BUT they only contain unique values

a = {1,2,3}
print('type is', type(a))

arry = [1,1,2,2,3,3,4,5]
print('let me be a set', set(arry))

# NOTE: please remember that set and dictionary order does not matter.
c_set = {'sailun', 'nguyen', 'bloo'}

c_set.add('sailuny')
c_set.add('saiLUN')
c_set.add(1234)
c_set.add(81489)
c_set.add('sailun')

print('set', c_set)

# im going to loop through c_set
for i in c_set:
    print('item', i)

