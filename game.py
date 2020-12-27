# ==============================================================
# Title: Escape Game
# Author: Daniel Lisle
# Synopsis: Escape a creepy house while being hunted by an enemy.
# --Four lock combations are needed to unlock the front door and escape.
# --Combinations are hidden in objects on each floor.
# --Enemy may detect you when your flashlight is on.
# ============================================================= */=
from hfile import *

floor = randint(0,3)
actions = 0
lightOn = False
lightToggled = False
moved = True
combosFound = ['False', 'False', 'False', 'False']
outcome = 0

map = makeMap();

print("\nYou don't remember how you got here, but have a feeling you shouldn't stay.  And you think you hear someone lurking around...\n")
print("\nCONTROLS: Enter...\n 'w' to move up a floor\n 's' to move down\n")
print(" 'f' to toggle flashlight\n 'e' to inspect an object\n 'q' to quit\n")
print(" '1','2', or '3' to choose object when prompted\n")
print("\n============ ESCAPE GAME =============\n\n")

while(outcome == 0):
    # Part 1: State
    if(moved):
        printFloor(floor)

    if(moved or lightToggled):
        if(lightOn):
            if(floor == 1):
                print("The front door is locked by four padlocks. ",end='')
                print("You see the following objects: ",end='')
            printObjects(map[floor]);
        else:
            print("It's too dark to see anything. ",end='')

    moved = False;
    lightToggled = False;

    # Part 2: Action
    print("You decide to ... ",end='');
    currentAction = input()
    print()

    # Part 3: Change
