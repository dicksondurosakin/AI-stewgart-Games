import random
import time

def display_intro():
    print('''You are in a land full of dragons,
    in front of you see two caves, in one cave,
    the dragon is friendly and will share his treasure with you.
    The other dragon is greedy and hungry, and will eat you on sight.
''')

def choose_cave():
    cave = ''
    while cave != "1" and cave != "2":
        cave = input("Which cave do you want to go? (1 or 2) ")
    return cave

def check_cave():
    friendly_cave = str(random.randint(1,2))
    user_choice = choose_cave()
    time.sleep(2)
    print("You are approaching the cave...")
    time.sleep(2)
    print("It is dark and spooky....")
    time.sleep(2)
    print("A large lion jumps in front of you, opens its mouth and ........")
    time.sleep(2)
    if friendly_cave == user_choice:
        print("He gives you he's treasures")
    else:
        print("He gobbles you down in one bite")

play_again = "yes"
while play_again == "yes":
    display_intro()
    check_cave()

    play_again = input("Do you want to play again? ('yes' or 'no')")
    print()
