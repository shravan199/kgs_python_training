fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

mylist = list(())

for fruit in fruits:
  if 'e' in fruit:
    mylist.append(fruit)
    
    
print(mylist)

print(fruits[1:4])

print('removing item')
print(mylist.pop(1))

print('clear items')
print(mylist.clear())

print('\nadding an item')
mylist.append('item1')
print(mylist)
mylist.insert(0, 'item2')
print(mylist)
mylist.remove('item1')
print(mylist) # item 2
