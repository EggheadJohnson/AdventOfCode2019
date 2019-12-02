import os
from intcode import intCodeComputer

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

permanent_input = inpt.readline()

for noun in range(0, 100):
    for verb in range(0, 100):
        icc = intCodeComputer(permanent_input)
        icc.operations[1] = noun
        icc.operations[2] = verb
        result = icc.run()
        if result == 19690720:
            print noun, verb, 100 * noun + verb
