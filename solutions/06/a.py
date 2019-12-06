import os, collections

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

orbit_maps = {}
left_side_planets = set()
right_side_planets = set()

for line in inpt:
    planet_a, planet_b = line.strip().split(')')
    left_side_planets.add(planet_a)
    right_side_planets.add(planet_b)
    if planet_a not in orbit_maps:
        orbit_maps[planet_a] = set()
    if planet_b not in orbit_maps:
        orbit_maps[planet_b] = set()
    orbit_maps[planet_a].add(planet_b)

first_planet = left_side_planets - right_side_planets
first_planet = first_planet.pop()

def getTotal(orbit_map, first_planet, total, depth = 1):
    for planet in orbit_map[first_planet]:
        total += depth
        total = getTotal(orbit_map, planet, total, depth + 1)
    return total


total = 0

print getTotal(orbit_maps, first_planet, total)
