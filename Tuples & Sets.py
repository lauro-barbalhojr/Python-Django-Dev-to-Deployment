#A tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
#Using constructor
#fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

#Get single value
print(fruit_tuple[1])

#Can not change value
#fruit_tuple[1] = 'Grape'
#print(fruit_tuple)

#Tuples  with one value should have trailing comma
#fruit_tuple_2 = ('Apple',)
#del fruit_tuple_2

#print(fruit_tuple_2)


#A set is a collection which is unordered and unindexed. No duplicate members

#Create set
fruit_set = {'Apple', 'Orange', 'Mango'}

#Check if in set
print('Apples' in fruit_set)

#Add to set
fruit_set.add('Grape')
print(fruit_set)

#Remove from set
fruit_set.remove('Grape')
print(fruit_set)

#Clear set
#fruit_set.clear()
print(fruit_set)


#Delete set
#del fruit_set
#print(fruit_set)
