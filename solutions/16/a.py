import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

def buildPattern(element = 1, length = 10):
    base = [0, 1, 0, -1]
    output = []
    ctr = 0
    for i in range(1, length + 2):
        output.append(base[ctr])
        if i%element == 0:
            ctr += 1
        ctr %= 4
    return output[1:]

def prepInput(inpt):
    return map(int, list(inpt.strip()))

def getNextRound(input):
    output = []
    for i in range(len(input)):
        pattern = buildPattern(i+1, len(input))
        runningTotal = 0
        for j, c in enumerate(input):
            runningTotal += c * pattern[j]
        output.append(abs(runningTotal)%10)
    return output

# print getNextRound([1,2,3,4,5,6,7,8])

# print buildPattern(), len(buildPattern())
# print buildPattern(2), len(buildPattern(2))
# print buildPattern(3), len(buildPattern(3))

def runPartA(inpt, rounds):
    inpt = prepInput(inpt.readline())
    for i in range(rounds):
        inpt = getNextRound(inpt)
    return inpt

# print ''.join(map(str, runPartA(inpt, 10000)))
