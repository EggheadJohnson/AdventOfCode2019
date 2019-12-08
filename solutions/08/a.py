import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

def layerize(str, size):
    layers = []
    for i in range(len(str)/size):
        layers.append(str[i * size : i * size + size])
    return layers

code = inpt.readline()

height = 6
width = 25

layers = layerize(code, height*width)

counts = []

for l in layers:
    counts.append({
        '0': l.count('0'),
        '1': l.count('1'),
        '2': l.count('2'),
    })

print counts

min_zeros = None
mult = None

for c in counts:
    if not min_zeros or c['0'] < min_zeros:
        mult = c['1'] * c['2']
        min_zeros = c['0']

print min_zeros, mult
