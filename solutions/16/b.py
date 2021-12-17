import os, a

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/b.in.txt"

inpt = open(input_path, 'r')
outp = open('b.out.txt', 'w')

def runPartB(inpt, rounds = 100):
    inpt = a.prepInput(inpt.readline())
    extended_inpt = []
    for x in range(10000):
        extended_inpt.extend(inpt)
    for i in range(rounds):
        print i
        inpt = a.getNextRound(extended_inpt)
    return inpt

print outp.write(''.join(map(str, runPartB(inpt, 100))))
