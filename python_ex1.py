applicant = input('Name: ')
person = applicant
print('\t which department do you work in?')

department = input('Department: ')
place = department



print (person.upper() + " works in " + department.upper())

print('{0} works in {1}' .format(person, place))


my_list = ["dummy","where","cock",1,2,4]

print('how does this work {}'.format(my_list[2]))

my_list.pop(2)
print(my_list)
my_list.sort()
print (my_list)