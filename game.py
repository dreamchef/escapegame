# ==============================================================
# Title: Escape Game
# Author: Daniel Lisle
# Synopsis: Escape a creepy house while being hunted by an enemy.
# --Four lock combations are needed to unlock the front door and escape.
# --Combinations are hidden in objects on each floor.
# --Enemy may detect you when your flashlight is on.
# ============================================================= */
from random import randint

objects = ['mirror',
        'painting',
        'chest',
        'bookshelf',
        'cage',
        'piano',
        'couch',
        'cabinet',
        'table',
        'desk',
        'barrel',
        'armchair']

# objectsMap

floor = randint(0,4)
#currentAction
actions = 0
lightOn = False
lightToggled = False
moved = True
combosFound = ['False', 'False', 'False', 'False']
escaped = False
caught = False

print("\nYou don't remember how you got here, but have a feeling you shouldn't stay.  And you think you hear someone lurking around...\n")
print("\nCONTROLS: Enter...\n 'w' to move up a floor\n 's' to move down\n")
print(" 'f' to toggle flashlight\n 'e' to inspect an object\n 'q' to quit\n")
print(" '1','2', or '3' to choose object when prompted\n")
print("\n============ ESCAPE GAME =============\n\n")
