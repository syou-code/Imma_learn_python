def add_two_numbers(num1, num2):
    return int(num1) + int(num2)

print('please pass in a number:')
a = input()

print('just another number')
b = input()
add = add_two_numbers(a, b)

print('sum:', add)
