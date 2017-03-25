# Write an equation that uses multiplication, division, an exponent,
# addition, and subtraction that is equal to 100.25

x1 = 401.0/4  # division
print(x1)
x2 = 20.05 * 5  # multiplication
print(x2)
x3 = 100 + 0.25  # addition
print(x3)
x4 = 200 - 99.75  # subrtaction
print(x4)

# print statements with arithmetic

print('What is the value of the expression 4 * (6 + 5)')  # lets print stuff
print('The value is: {}' .format(4 * (6 + 5)))  # lets print stuff

print('What is the value of the expression 4 * 6 + 5')  # lets print stuff
print('The Value is: {}'.format(4*6+5))  # lets print stuff

print('What is the value of the expression 4 + 6 * 5')  # lets print stuff
print('The value is: {}'.format(4+6*5))  # lets print stuff

# printing with strings
string1 = 'hello'
print(string1[1])  # prints what is located in locatoin '1'
print(string1[::-1])  # prints hello in reverse
print(string1[-1])  # prints the call from the end -1
print(string1[4])  # prints what is located in location 4

# build list two different ways
list1 = [1]*3  # creates list of a same number * 3
list2 = [1, 2, 3]  # basic method for creating lists
print(list1, list2)  # prints list1 & list2

# sets
set1 = set()  # create set
set1.add(22)  # add to set
set1.add(21)  # add to set
print(set1)  # print set1
set1.clear()  # clears set
print(set1)  # prints clear set

# dictionary
dict1 = {}
print(dict1)
del dict1

dict2 = {'words':'make', 'no':'sense'}  # dictionary created
print(dict2.keys())  # prints keys to dictionary
print(dict2['words'])  # prints value for first key
print(dict2['no'])  # prints value to second key

