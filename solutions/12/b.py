import os, copy
from a import Moon, updateOneMoon, updateAllMoons

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

moons = []

for line in inpt:
    new_moon = Moon(line)
    moons.append(new_moon)

initial_moon_position = copy.deepcopy(moons)

print reduce(lambda x, y: x + y.thisIsntReallyTotalEnergy(), moons, 0)

zeros = [
[],
[],
[],
[]
]

for x in range(2780):
    updateAllMoons(moons)
    for i in range(len(moons)):
        if moons[i].thisIsntReallyTotalEnergy() == 0:
            zeros[i].append(x)
    # print reduce(lambda x, y: x + y.thisIsntReallyTotalEnergy(), moons, 0)

for z in zeros:
    print z
    zb = []
    for b in range(1, len(z)):
        zb.append(z[b] - z[b-1])
    print zb
    za = []
    for a in range(1, len(zb)):
        za.append(zb[a] - zb[a-1])
    print za
