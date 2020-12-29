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
lightSwitched = False
moved = True
comboFound = ['False', 'False', 'False', 'False']
outcome = 0

map = makeMap();

print("\nYou don't remember how you got here, but have a feeling you shouldn't stay.  And you think you hear someone lurking around...\n")
print("\nACTIONS:\n 'move up'\n 'move down'\n")
print(" 'switch' (flashlight on/off)\n 'inspect' (an object)\n 'quit'\n")
print(" '1','2', or '3' to choose object when prompted\n")
print("\n============ ESCAPE GAME =============\n\n")

while(outcome == 0):
    # State information
    if(moved):
        printFloor(floor)

    if(moved or lightSwitched):
        if(lightOn):
            if(floor == 1):
                print("The front door is locked by four padlocks. ",end='')
                print("You see the following objects: ",end='')
            printObjects(map[floor]);
        else:
            print("It's too dark to see anything. ",end='')

    moved = False;
    lightSwitched = False;

    # Action selection
    print("You decide to ... ",end='');
    action = input()
    print()

    # Change information
    if(action == 'move up' or action == 'move down'):
        newFloor = movePlayer(action,floor)
        moved = bool(abs(newFloor-floor))
        floor = newFloor
        if(lightOn == True):
            outcome = detected(map[floor])

    elif(action == 'inspect'):
        if(lightOn == True):
            print(" the ",end='')
            targetObject = int(input()) - 1
            if(targetObject >= 0 and targetObject < OBJECTS):
                print(map[floor][targetObject].name + ". ")
                if(map[floor][targetObject].combination == True):
                    print("Upon inspection you discover the hidden compartment.  Inside is a slip of paper with numbers written on it. ",end='')
                    comboFound[floor] = True
                else:
                    print("You inspect it but find nothing. ",end='')
            else:
                print("controls. ",end='')
            outcome = detected(map[floor])
        else:
            print(" an object, but it's too dark to see what's in the room.  Maybe if you turned on your flashlight... ",end='')

    elif(action == 'switch'):
        lightOn = switchLight(lightOn)
        lightSwitched = True

    elif(action == 'quit'):
        sys.exit(0)

    else:
        print("... review your options. ")

    # Endgame check
    if(floor == 1 and comboFound == ['True']*FLOORS and lightOn and outcome == 0):
        print("You approach the front door. Hands shaking, you start entering the combinations. ",end='')
        outcome = detected(map[floor])
        if(outcome == 0):
            outcome = 2

    actions += 1

displayOutcome(outcome,actions)
