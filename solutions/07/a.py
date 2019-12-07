import os,  sys, itertools
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../helpers')
import intcode

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

inpt = inpt.readline()


debugMode = len(sys.argv) > 1 and sys.argv[1]

max = None

# b = 0

for combo in itertools.permutations(range(5), 5):
    b = 0
    # print combo
    for c in combo:
        a = c
        icc = intcode.intCodeComputer(inpt, debugMode)
        icc.run([a, b])
        b = icc.output
    if not max or b > max:
        max = b

print max
# icc = intcode.intCodeComputer(inpt, debugMode)
#
# icc.run()
