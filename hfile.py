
WIN_W = 700
WIN_H = 1000
OFFSET = 50
FLOOR_H = 200
FLOOR_W = WIN_W-(OFFSET*3)

FLOORS = 4
OBJECTS = 3 #per floor
DETECTION = 25 #/100

from random import *
import sys

class Object:
    def __init__(self, name,combination):
        self.name = name
        self.combination = combination

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

def makeMap():
    shuffle(objects)

    map = [[Object('',False) for j in range(OBJECTS)] for i in range(FLOORS)]

    k=0
    for floor in map:
        for object in floor:
            object.name = objects[k]
            k += 1
        floor[randint(0,OBJECTS-1)].combination = True

    return map

def printFloor(floor):
    if floor == 0:
            print("You're now in the basement. ",end='')
    elif floor == 1:
            print("You're now on the ground floor. ",end='')
    elif floor == 2:
            print("You're now on the second floor. ",end='')
    elif floor == 3:
            print("You're now in the attic. ",end='')

def printObjects(objects):
    print("You see the following objects: ",end='')
    for i in range(len(objects)):
        print(" [" + str(i+1) + "] " + objects[i].name,end='')
    print(". ",end='');

def movePlayer(direction, floor):
    if (direction == 'move up'):
        if(floor > FLOORS-2):
            print("... move, but you're already on the top floor. ")
            return floor
        else:
            print("... sneak up the stairs. ")
            return floor + 1
    elif (direction == 'move down'):
        if(floor < 1):
            print("but you're already on the bottom floor. ")
            return floor
        else:
            print("... sneak down the stairs. ")
            return floor - 1
    else:
        print("DEBUG: Invalid direction")

def switchLight(lightOn):
    if(lightOn == True):
        print(" your flashlight off. ",end='')
    else:
        print(" your flashlight on. ",end='')
    return not lightOn

def detected(floor):
    if(randint(0,99) < 25):
        print("Then you hear someone approaching.  They must have seen your flashlight beam, so you switch it off. ",end='')
        print("From the three possible hiding spots: ",end='')
        printObjects(floor)
        print(", you choose ... ",end='')
        try:
            coverObjIdx = int(input()) - 1
            assert coverObjIdx >= 0 and coverObjIdx < OBJECTS
            elimObjIdx = randint(0,OBJECTS-1)
            if(floor[coverObjIdx].name == floor[elimObjIdx].name):
                return 1
            else:
                print("They walk to the other side of the room and look behind the " + floor[elimObjIdx].name + ". Finding nothing, they leave. You cautiously emerge and turn on your flashlight.",end='')
        except (ValueError, AssertionError):
            print("... nothing, you're frozen with fear.  Obviously that doesn't work out well for you.  Maybe review those option controls... ",end='')
            return 1
    return 0

def displayOutcome(outcome,actions):
    if(outcome == 1):
        print("\n\nYou no longer hear the lurker, despite straining your ears. ",end='')
        print("Suddenly, you feel a prick on the back of your neck and start to feel faint. ",end='')
        print("Above you... a shadowy figure... then... nothing... ",end='')
        print("\n\nAfter " + str(actions) + " actions, you were caught by the lurker. ",end='');
    else:
        print("\n\nAfter what seems like an eternity, you unlock all four locks. ",end='')
        print("You slip out the door and escape to freedom. \n\nYou completed the game in " + str(actions) + " actions. ",end='')
