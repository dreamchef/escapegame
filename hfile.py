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


def printFloor():
    return 0;
