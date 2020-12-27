FLOORS = 4
OBJECTS = 3

from random import *

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

    map = [[Object('',False)]*OBJECTS]*FLOORS

    i=0
    for floor in map:
        for object in floor:
            object.name = objects[i]
            i += 1
        floor[randint(0,2)].combination = True

    return map

def printFloor(floor):
    if floor == 0:
            print("You're now in the basement. ")
    elif floor == 1:
            print("You're now on the ground floor. ")
    elif floor == 2:
            print("You're now on the second floor. ")
    elif floor == 3:
            print("You're now in the attic. ")

def printObjects(objects):
    print("You see the following objects: ")
    for i in range(len(objects)):
        print(" " + str(i) + " " + objects[i].name)
    printf(". ");
