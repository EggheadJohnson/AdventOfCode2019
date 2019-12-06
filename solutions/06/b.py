import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

def buildReverseMap(inpt):
    you = None
    santa = None
    reverse_graph = {}
    for line in inpt:
        planet_a, planet_b = line.strip().split(')')
        if planet_b == 'YOU':
            you = planet_a
        elif planet_b == 'SAN':
            santa = planet_a
        else:
            if planet_b not in reverse_graph:
                reverse_graph[planet_b] = planet_a
            else:
                print "PANIC PANIC PANIC planet", planet_b, "was already present!!"
    return reverse_graph, you, santa

def findMyOrbits(reverse_graph, you):
    orbits = {
        you: 0
    }
    curr = you
    while curr in reverse_graph:
        next = reverse_graph[curr]
        orbits[next] = orbits[curr] + 1
        curr = next
    return orbits

def findSantasOrbitsAndOurIntersection(reverse_graph, my_orbits, santa):
    orbits = {
        santa: 0
    }
    curr = santa
    while curr in reverse_graph:
        if curr in my_orbits:
            return orbits[curr] + my_orbits[curr]
        next = reverse_graph[curr]
        orbits[next] = orbits[curr] + 1
        curr = next

reverse_graph, you, santa = buildReverseMap(inpt)

my_orbits = findMyOrbits(reverse_graph, you)

print findSantasOrbitsAndOurIntersection(reverse_graph, my_orbits, santa)
