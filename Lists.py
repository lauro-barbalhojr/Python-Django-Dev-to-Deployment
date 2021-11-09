#A list is a collection which is ordered and changeable. Allows duplicate members.

#Create a list
#numbers = [1,2,3,4,5]

#Using a constructor
numbers = list((1,2,3,4,5))
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
print(fruits)

#Get value
print(fruits[1])

#Get length
print(len(fruits))

#Append to list
fruits.append('Mangos')
print(fruits)

#Remove from list
fruits.remove('Grapes')
print(fruits)

#Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

#Remove from position
fruits.pop(3)
print(fruits)

#Reverse list
fruits.reverse()
print(fruits)

#Sort list
fruits.sort()
print(fruits)

#Reverse sort
fruits.sort(reverse=True)
print(fruits)