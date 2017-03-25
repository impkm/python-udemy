x = set()  # create a set
x.add(1)  # adds to set
print(x)  # prints set

x.add(2)  # adds to x
print(x)  # prints x

y = (2, 2, 2, 3, 4, 3, 5, 4, 4, 22, 32, 44)  # list with ints that repeat
x.update(y)  # updates set 'x' with list 'y'
print(set(x))  # prints updated list for 'x'
print(set(y))  # prints unique sets from list

print(1 == 2)  # prints false
print(1 != 2)  # prints true

if 3 != 3:  # if/else statement with boolean
    print('This is true')
else:
    print('this is false')

if len('words') > len('hippos'):  # if/else statement with boolean using string
    print('Words is the larger word')
else:
    print('Hippos is the larger word')

b = None  # assigns placement holder for variable
print(b)  # prints None

