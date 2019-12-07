import os,  sys, itertools
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../helpers')
import intcode

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')

inpt = inpt.readline()


debugMode = len(sys.argv) > 1 and sys.argv[1]

max = None

# b = 0

for combo in itertools.permutations(range(5, 10), 5):
# for combo in [(9, 8, 7, 6, 5)]:
    b = 0
    # print combo
    A = intcode.intCodeComputer(inpt, combo[0], debugMode)
    B = intcode.intCodeComputer(inpt, combo[1], debugMode)
    C = intcode.intCodeComputer(inpt, combo[2], debugMode)
    D = intcode.intCodeComputer(inpt, combo[3], debugMode)
    E = intcode.intCodeComputer(inpt, combo[4], debugMode)

    while not E.stopped:
        A.run([b])
        B.run([A.output])
        C.run([B.output])
        D.run([C.output])
        E.run([D.output])
        b = E.output

    if not max or b > max:
        max = b

print max
# icc = intcode.intCodeComputer(inpt, debugMode)
#
# icc.run()
