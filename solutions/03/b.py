import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

def buildPathFromSteps(steps):
    position = [0, 0]
    directions = {
        'L': [-1, 0],
        'R': [1,  0],
        'D': [0, -1],
        'U': [0,  1],
    }
    positions = {}
    step_counter = 0
    for step in steps:
        direction = directions[step[0]]
        count = int(step[1:])
        for i in range(count):
            step_counter += 1
            position[0] += direction[0]
            position[1] += direction[1]
            positions[tuple(position)] = step_counter
    return positions

def manhattanDist(position):
    return abs(position[0]) + abs(position[1])

def findClosest(first_wire, second_wire):

    closest = None
    for pos in first_wire:
        if pos in second_wire and (not closest or first_wire[pos] + second_wire[pos] < first_wire[closest] + second_wire[closest]):
            closest = pos
    return first_wire[closest] + second_wire[closest]

first_wire = buildPathFromSteps(inpt.readline().split(','))
second_wire = buildPathFromSteps(inpt.readline().split(','))
# print first_wire
# print second_wire
#
# print first_wire & second_wire
closest = findClosest(first_wire, second_wire)
print closest
