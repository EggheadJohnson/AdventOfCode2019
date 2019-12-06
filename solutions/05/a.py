import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../helpers')
import intcode

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

icc = intcode.intCodeComputer(inpt.readline())

# icc.printOperations()
icc.run()
# icc.printOperations()
