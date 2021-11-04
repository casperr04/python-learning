# For loops loop through an array or number range
# len lets you get amount of strings in an array

friends = ["Joe", "Jimmy", "Luke"]
for letter in "Bad Business":
    print(letter)
for friend in friends:
    print(friend)
for index in range(10):
    print(index)
for index2 in range(13, 23):
    print(index2)
print(len(friends))
for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")