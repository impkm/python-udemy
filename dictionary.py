my_dict = {'username':'paul', 'Password':'12334321'} # my first dictionary
#my_dict['username'] # gives value to first key

print(my_dict['username']) # prints value to username
print(my_dict['Password']) # prints value to password
print(my_dict.keys()) # prints keys to dictionary

my_dict.clear() # clear
print(my_dict) # prints brackets

dict2 = {} # creates new dictionary
print(dict2) # prints empty dictionary

dict2['jon'] = 43 # adds to dictionary
dict2['will'] = 32 # adds to dictionary
print(dict2) # prints new dictionary

print(dict2.keys()) # prints new dictionary keys

dict1 = {'k1': 23, 'k2': 33, 'k3':'paul'}
print(dict1['k1']) # prints value in 1st key
print(dict1.keys()) # prints keys from dictionary
print(dict1.values()) # prints values from keys
dict1['k1'] += 100 # adds 100 to k1
print(dict1['k1']) # prints k1 new value
print(dict1) # prints

dict3 = {'inception': {'leo': {'titanic': {'rose'}}}} # dictionary inception
print(dict3) # prints dictionary
print(dict3['inception'] ['leo'] ['titanic']) # prints value to 3rd dictionary

print('This is the length of my first list %d' % len(my_dict)) # prints length of first list
print('This is the length of my second list %d' %len(dict2)) #prints length of second list
print('This is the length of my third list %d' %len(dict1)) #prints length of dict1
print('This is the length of my fourth list %d' %len(dict3)) #prints length of dict3

my_dict.update(dict2) # updates my_dict with dict2
print(my_dict) # prints updated dictionary with dict2

my_dict.update({'how':23}) # adds to dictionary
print(my_dict) # prints updated dictionary

