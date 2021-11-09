# Code can be made a lot shorter with functions and maybe a dictionary?
# Needs refactoring
import random

ai_guess = random.randrange(0, 3)
rock = 0
paper = 1
scissors = 2
human_guess_input = input("What's your guess? (rock/paper/scissors)")
human_guess = 3
human_win = 0
if "rock" in human_guess_input:
    human_guess = 0
elif "paper" in human_guess_input:
    human_guess = 1
else:
    human_guess = 2

if ai_guess == 0:
    print("AI guesses.. Rock!")
    if human_guess == 0:
        human_win += 1
    elif human_guess == 1:
        human_win += 2

if ai_guess == 1:
    print("AI guesses.. Paper!")
    if human_guess == 1:
        human_win += 1
    elif human_guess == 2:
        human_win += 2

if ai_guess == 2:
    print("AI guesses.. Scissors!")
    if human_guess == 2:
        human_win += 1
    elif human_guess == 0:
        human_win += 2

if human_win == 1:
    print("Draw!")
elif human_win == 2:
    print("You won!")
else:
    print("You Lost!")




