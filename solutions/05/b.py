import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../helpers')
import intcode

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

inpt = inpt.readline()

debugMode = len(sys.argv) > 1 and sys.argv[1]


icc = intcode.intCodeComputer(inpt, debugMode)

# icc.printOperations()
icc.run()
# icc.printOperations()
