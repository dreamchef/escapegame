FLOORS = 4
OBJECTS = 3

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

def detected(floor,map):
    #TODO: implement
    return 0
