# \n in string breaks the string and outputs text in two different lines
print("Engineer\nGaming\n")

# An example of \n in haiku text
print("The west wind whispered,\nAnd touched the eyelids of spring:\nHer eyes, Primroses\n")

# \" lets you put quotation marks in string
print("And the man said \"Why should I care about this?\"\n")

# You can print a variable by just putting its name in print()

phrase = "Gaming"
print("Engineer " + phrase + "\n")

# Some functions allow you to edit strings

secret_word = "SANTA"
print(secret_word.lower() + "\n")
print(secret_word.upper() + "\n")
print(secret_word.isupper())
print(secret_word.islower())

# Multiple functions can be in one line of code

print(secret_word.lower().islower())

# len function can count how long a string is

print(len(secret_word))

# [] lets you specify which index to print in string, starting from 0
print(secret_word[0])
print(secret_word[1])

# .index lets you find the index of a letter in a string, for example S = 0, A =1 etc
# .index will find the first letter in the string, ignoring the rest
print(secret_word.index("S"))
print(secret_word.index("NTA"))

# if .index function is unable to find specified letter in string, it will cause an error

# .replace function lets you replace words in string
print(secret_word.replace("TA", "TUS"))
