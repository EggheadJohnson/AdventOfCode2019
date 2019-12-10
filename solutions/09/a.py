import os, sys, itertools
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../helpers')
import intcode

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

debugMode = len(sys.argv) > 1 and sys.argv[1]

inpt = open(input_path, 'r')

icc = intcode.intCodeComputer(inpt.readline(), None, debugMode, 500)
# icc.printOperations()
icc.run()
# icc.printOperations()
