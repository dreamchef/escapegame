FLOORS = 4
POS = 3

from random import *

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

    map = [[0]*POS]*FLOORS

    i=0
    for floor in map:
        for pos in floor:
            pos = objects[i]
            i += 1

    return map


def printFloor():
    return 0;
