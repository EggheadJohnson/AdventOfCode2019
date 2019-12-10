import os
from math import atan, tan, pi, atan2

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

pairs = []

for x in range(-10, 10):
    for y in range(-10, 10):
        pairs.append((y, x))

for s in sorted(pairs, key=lambda s: atan2(s[0], s[1])):
    print s, atan2(s[0], s[1])
