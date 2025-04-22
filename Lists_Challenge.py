# Create a list

myList = ["Batman", "Spider-Man", "Wolverine", "Hulk", "Phoenix"]

#Loop Through list

for x in myList:
    print(x)

# Append() Method

myList.append ("Kitty Pryde")
print(myList)
['Batman', 'Spider-Man', 'Wolverine', 'Hulk', 'Phoenix', 'Kitty Pryde']

# Copy()

thislist = ["Batman", "Spider-Man", "Wolverine", "Hulk", "Phoenix", "Kitty Pryde"]
myList = thislist.copy()
print(myList)
['Batman', 'Spider-Man', 'Wolverine', 'Hulk', 'Phoenix', 'Kitty Pryde']

# Concatenate two lists

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
concatenated_list = list1 + list2
print(concatenated_list)
[1, 2, 3, 4, 5, 6, 7, 8]

# Reverse() method

print(myList)
['Batman', 'Spider-Man', 'Wolverine', 'Hulk', 'Phoenix', 'Kitty Pryde']
myList.reverse()
print(myList)
['Kitty Pryde', 'Phoenix', 'Hulk', 'Wolverine', 'Spider-Man', 'Batman']
