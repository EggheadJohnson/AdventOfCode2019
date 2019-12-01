import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

def getFuelReqs(mass):
    if mass <= 0:
        return 0
    return mass + getFuelReqs(mass/3 - 2)


tot = 0
fuel = 0

for i in inpt:
    fuel += getFuelReqs(int(i) / 3 - 2)

print fuel
