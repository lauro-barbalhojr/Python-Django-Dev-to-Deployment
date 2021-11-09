#Strings in python are surrounded by either single or double quotation marks.
# Let's look at string formatting and some string methods

name = 'Lauro'
age = 25

#Concatenate

print('Hello I am ' + name + ' and I am ' + str(age))

#Arguments by position
#print('{}, {}, {}'.format('a','b','c'))
#print('{1}, {2}, {0}'.format('a','b','c'))

#Arguments by name
#print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings
#print(f'My name is {name} and I am {age}')

s = 'hello there world'

#Capitalize first letter
print(s.capitalize())

#Make all upper case
print(s.upper())

#Make all lower case
print(s.lower())

#Swap case
print(s.swapcase())

#Get length
print(len(s))

#Replace
print(s.replace('world', 'everyone'))

#Count
sub = 'h'
print(s.count(sub))