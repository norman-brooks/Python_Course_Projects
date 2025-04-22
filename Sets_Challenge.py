# Create a Set

mySet = {"dog", "cat", "bird"}
print(mySet)
{'bird', 'cat', 'dog'}

# Add() method

mySet.add("hamster")
print(mySet)
{'bird', 'cat', 'hamster', 'dog'}
# Remove() method

mySet.remove("bird")
print(mySet)
{'cat', 'hamster', 'dog'}
# Difference() method
set1 = {"Eagles", "Phillies", "Sixers"}
set2 = {"Eagles", "Flyers", "Union"}
z = set1.difference(set2)
print(z)
{'Phillies', 'Sixers'}
z = set2.difference(set1)
print(z)
{'Union', 'Flyers'}
