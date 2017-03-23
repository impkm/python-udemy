my_list = [12, 334, 34, 54, 54, 32] #my first list
print(my_list) #prints my first list

my_list.pop() #removes last item in list
print(my_list) #prints new list

my_list.remove(12) #removes what is called.
print(my_list) #prints my list

print(len(my_list)) #prints length of list

my_list2 = [4345, 'comment', 'how']

print('{} am i doing this'.format(my_list2[2])) #prints from a list at 'second' location
print('this is where i {}!'.format(my_list2[1])) #prints from list at 'one' location
print('i wish to earn this much a month {}'.format(my_list2[0])) #prints from list at 'zero' location

my_list3 = my_list + my_list2 #my_list3 is a combination of my_list and my_list2
print(my_list3) #my_list3 is printed in order received from previous line

my_list3.append('do it') #adds to list at end
print(my_list3)

my_list3.pop(0) #removes first list element
print(my_list3)
print(my_list)

print cmp(my_list3, my_list) #compares list3 to list1
print('this is my value in my first list: {}'.format(max(my_list)))

List2 = [3234, 3243, 443, 34332, 44444] #new list
List2.pop(2) #removes second element
print(List2) #prints list without 'second' element







