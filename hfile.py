FLOORS = 4
POS = 3

from random import *

class Object:
    def __init__(self, name,combination)
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

    map = [[0]*POS]*FLOORS

    i=0
    for floor in map:
        for pos in floors:
            pos = Object(objects[i],false)
            i += 1
        floor[randint(0,2)].combination = true;


    return map


def printFloor():
    return 0;
