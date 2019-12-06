import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

def isValidPW(pw):
    seenDouble = False
    for i, c in enumerate(list(pw)[1:]):
        if c == pw[i]:
            seenDouble = True
        if int(c) < int(pw[i]):
            return False
    return seenDouble

def run(lowerUpper):
    validCount = 0
    lower, upper = lowerUpper.split('-')
    # print lower, upper, int(lower), int(upper)
    for i in range(int(lower), int(upper)+1):
        # print i, isValidPW(str(i))
        if isValidPW(str(i)):
            validCount += 1
    return validCount

print run(inpt.readline())
# print isValidPW('191')
