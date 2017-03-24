t = (1, 3, 2, 3) # created my first tuple
t.index(3) #locates first 3 in tuple
print(t.index(3)) # prints first 3 in tuple

print(t.count(2)) # prints how many times '2' appears
print(t.count(3)) # prints how many times '3' appears

list1 = [1, 3, 2, 3, 4, 3, 3,] # created list to convert to tuple
new_tuple = tuple(list1) # converted list to tuple
print(new_tuple) # print new_tuple
list1.insert(3,4)

print(len(new_tuple)) # prints length of tuple
print(list1) # prints list1 with new insertion

print(new_tuple)
print(new_tuple.index(3, 6))
