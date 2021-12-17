import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

class Moon:
    def __init__(self, starting_position_string):
        # print starting_position_string
        starting_position_string = starting_position_string.strip()[1:-1]
        # print starting_position_string
        starting_position_array = starting_position_string.split(',')
        # print starting_position_array
        starting_position_array = map(lambda x: x.strip(), starting_position_array)
        # print starting_position_array
        starting_position_array = map(lambda x: int(x[2:]), starting_position_array)
        # print starting_position_array
        self.x = starting_position_array[0]
        self.y = starting_position_array[1]
        self.z = starting_position_array[2]

        self.vx = 0
        self.vy = 0
        self.vz = 0

        self.ax = 0
        self.ay = 0
        self.az = 0
    def updateAccelerations(self, other_moon):
        if other_moon.x != self.x:
            self.ax += (other_moon.x - self.x) / abs(other_moon.x - self.x)
        if other_moon.y != self.y:
            self.ay += (other_moon.y - self.y) / abs(other_moon.y - self.y)
        if other_moon.z != self.z:
            self.az += (other_moon.z - self.z) / abs(other_moon.z - self.z)
    def resetAcceleration(self):
        self.ax = 0
        self.ay = 0
        self.az = 0
    def updateVelocities(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
    def updatePositions(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
    def thisIsntReallyPotentialEnergy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)
    def thisIsntReallyKineticEnergy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)
    def thisIsntReallyTotalEnergy(self):
        return self.thisIsntReallyPotentialEnergy() * self.thisIsntReallyKineticEnergy()
    def printThisMoon(self):
        print "<x: {}, y: {}, z: {}> <vx: {}, vy: {}, vz: {}> <ax: {}, ay: {}, az: {}>".format(self.x, self.y, self.z, self.vx, self.vy, self.vz, self.ax, self.ay, self.az)

def updateOneMoon(moon, other_moons):
    for other_moon in other_moons:
        moon.updateAccelerations(other_moon)


def updateAllMoons(moons):
    for i, moon in enumerate(moons):
        moon.resetAcceleration()
        updateOneMoon(moon, moons[:i]+moons[i+1:])
    for moon in moons:
        moon.updateVelocities()
        moon.updatePositions()

# moons = []
#
# for line in inpt:
#     new_moon = Moon(line)
#     moons.append(new_moon)
#
# for moon in moons:
#     moon.printThisMoon()
#
# for x in range(1000):
#     updateAllMoons(moons)
# print
#
# for moon in moons:
#     moon.printThisMoon()
#
# print reduce(lambda x, y: x + y.thisIsntReallyTotalEnergy(), moons, 0)


# for moon in moons:
#     print moon.thisIsntReallyPotentialEnergy(), moon.thisIsntReallyKineticEnergy(), moon.thisIsntReallyTotalEnergy()
