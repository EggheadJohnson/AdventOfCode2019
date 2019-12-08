import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

def layerize(str, size):
    layers = []
    for i in range(len(str)/size):
        layers.append(str[i * size : i * size + size])
    return layers

def stacklayers(layers):
    final_image = ''
    for i in range(len(layers[0])):
        pixel = '2'
        for j in range(len(layers)):
            if pixel == '2' and layers[j][i] != '2':
                pixel = layers[j][i]
        final_image += pixel
    return final_image

height = 6
width = 25

layers = layerize(inpt.readline(), height * width)

# print layers

stacked = stacklayers(layers)

# print stacked

relayered = layerize(stacked, width)

# print relayered

for line in relayered:
    l = ''
    for c in line:
        if c == '0':
            l += ' '
        else:
            l += '#'
    print l
