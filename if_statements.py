# if statements are statements that can either be true or false

is_male = False
is_hungry = True

if is_male:
    print("I'm male")
else:
    print("I am a female")
if is_hungry:
    print("I am hungry.")
else:
    print("I am not hungry.")

if is_male or is_hungry:
    print("You are either hungry or a male")
else:
    print("You are neither hungry or male.")
if is_male and is_hungry:
    print("You are definitely hungry and a male")
elif is_male and not(is_hungry):
    print("You are a male but you are not hungry.")
elif not(is_male) and (is_hungry):
    print("You are not a male, but you are hungry.")

# elif stands for else if
