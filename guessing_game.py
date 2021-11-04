secret_word = "bonanza"
guess = ""
attempts = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if attempts < guess_limit:
       guess = input("Enter guess: ")
       attempts += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lose!")
else:
    print("Congratulations, you won!")
