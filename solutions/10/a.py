import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

def findAllVisibleForPoint(point, asteroid_map):
    all_visible = set()
    for i, row in enumerate(asteroid_map):
        for j, spot in enumerate(row):
            if spot == '#' and (i, j) != point:
                addReducedToSet(point, (i, j), all_visible)
    return all_visible

def addReducedToSet(point, spot, all_visible):
    x = point[0] - spot[0]
    y = point[1] - spot[1]

    x1, y1 = reduceFraction(x, y)
    # print point, spot, (x, y), (x1, y1)
    all_visible.add((x1, y1))

def reduceFraction(x, y):
    c = 2
    if x == 0 and y != 0:
        return 0, 1 * y / abs(y)
    if y == 0 and x != 0:
        return 1 * x / abs(x), 0
    if x == 0 and y == 0:
        print "THAT SHOULDN'T HAVE HAPPENED"
        return 0, 0
    while c <= min(abs(x), abs(y)):
        if x % c == 0 and y % c == 0:
            x /= c
            y /= c
            c = 2
        else:
            c += 1
    return x, y

def findAllVisibilitiesForAllPoints(asteroid_map):
    results = {}
    for i, row in enumerate(asteroid_map):
        for j, spot in enumerate(row):
            if spot == '#':
                results[(i, j)] = findAllVisibleForPoint((i, j), asteroid_map)
    return results

def buildAsteroidMap(inpt):
    asteroid_map = []
    for line in inpt:
        asteroid_map.append(list(line.strip()))
    return asteroid_map

def findBestAsteroid(visibilities):
    max_point = None
    for point in visibilities:
        if not max_point or len(visibilities[point]) > len(visibilities[max_point]):
            max_point = point
    return max_point, len(visibilities[max_point])

asteroid_map = buildAsteroidMap(inpt)

# print asteroid_map

result = findAllVisibilitiesForAllPoints(asteroid_map)
#
# # for spot in result:
# #     print spot, len(result[spot]), result[spot]
#
print findBestAsteroid(result)
