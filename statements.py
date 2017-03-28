# if statements
if len('greater') > len('less'):  # simple if statement checking length of string
    print('first option')
else:
    print('second option')

x = 23
y = 44

if x >= y:  # if else statement checking which is greater
    print('x: {} is greater than y: {}'.format(x, y))
else:
    print('x: {} is not greater than y: {}'.format(x, y))

if y >= x:
    print('Y: {} is greater than X: {}'.format(y,x))
else:
    print('Y: {} is not greater than X: {}'.format(y,x))

z = 22
if x == y:  # this is not true
    print('They are equal')
elif y <= z:  # this is not true
    print('Y is less than Z')
else:  # this is true
    print('Y is not equal to X and Y is not less than Z')


if x > z and y > z:  # if statement checking both conditions
    print('X and Y are greater than Z')
else:  # this will not print
    print('X and Y are less than Z')

