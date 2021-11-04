
lucky_numbers = [3, 6, 23, 32, 40, 85]
friends = ["Joe", "Megan", "Pierre", "Nancy", "Elizabeth", "Hilda", "Megan"]
# .extend lets you to add a list to a different list
#friends.extend(lucky_numbers)
# .append lets you add a string into a list
friends.append("Rogan")
# .insert lets you add a string into a list, specifying at what index to insert it
friends.insert(3, "Gary")
# .remove lets you remove a string from a list
friends.remove("Elizabeth")
# .clear lets you clear an entire list
# friends.clear()
# .pop lets you remove the last string from a list
friends.pop()
# .index lets you find an index of a specified string
print(friends.index("Megan"))
print(friends.index("Nancy"))
# .count lets you count all of the same strings in a list
print(friends.count("Megan"))
# .sort will put the list in alphabetical order
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
# .reverse will reverse a list
lucky_numbers.reverse()
print(lucky_numbers)
# .copy will copy a list
friends2 = friends.copy()
print(friends2)