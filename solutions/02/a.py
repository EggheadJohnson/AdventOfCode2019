import os
from intcode import intCodeComputer

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')



# print inpt.readline()
icc = intCodeComputer(inpt.readline())
icc.printOperations()
icc.run()
icc.printOperations()
