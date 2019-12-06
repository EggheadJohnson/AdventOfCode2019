import os
from collections import Set

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

def buildPathFromSteps(steps):
    position = [0, 0]
    directions = {
        'L': [-1, 0],
        'R': [1,  0],
        'D': [0, -1],
        'U': [0,  1],
    }
    positions = set()
    for step in steps:
        direction = directions[step[0]]
        count = int(step[1:])
        for i in range(count):
            position[0] += direction[0]
            position[1] += direction[1]
            positions.add(tuple(position))
    return positions

def manhattanDist(position):
    return abs(position[0]) + abs(position[1])

def findClosest(first_wire, second_wire):
    intersections = first_wire & second_wire
    closest = None
    for i in intersections:
        if not closest or manhattanDist(i) < manhattanDist(closest):
            closest = i
    return closest

first_wire = buildPathFromSteps(inpt.readline().split(','))
second_wire = buildPathFromSteps(inpt.readline().split(','))
# print first_wire
# print second_wire
#
# print first_wire & second_wire
closest = findClosest(first_wire, second_wire)
print closest, manhattanDist(closest)
