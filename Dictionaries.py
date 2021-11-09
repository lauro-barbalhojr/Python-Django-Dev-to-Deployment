# A Dictionary is a collection which is unordered, changeable and indexed. 
# No duplicate members.

# Simple dictionary
person = {
    'first_name': 'Jack',
    'last_name': 'Sparrow',
    'age':35
}
print(person)

# Using a constructor
person = dict(first_name='Jack', last_name='Sparrow', age=35)
print(person)

# Access Values
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone']='9876-5432'

# Get keys
print(person.keys())

# Get Items
print(person.items())

# Make copy
person2= person.copy()
person2['city'] = 'London'
print(person2)

# Remove item 
#del(person['age'])
#person.pop('phone')

# Clear
#person.clear()

# Get length
print(len(person2))

print(person)

# List of dict
people = [
    {'name': 'Martha', 'age': 40},
    {'name': 'Bob', 'age': 20}
]

print(people[1]['name'])