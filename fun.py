name_list = ["Joe", "Moe", "Doe"]
names_total = 0
letters_total = 0

for name in name_list:
    names_total += 1
    for letter in name:
        letters_total += 1

print(letters_total, names_total)

