import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

def isValidPW(pw):
    seenDouble = False
    streakCounter = 1
    for i, c in enumerate(list(pw)[1:]):

        if c == pw[i]:
            streakCounter += 1
        if c != pw[i]:
            if streakCounter == 2:
                seenDouble = True
            streakCounter = 1
        if int(c) < int(pw[i]):
            return False
    return seenDouble or streakCounter == 2

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
# print isValidPW('112233')
# print isValidPW('123444')
# print isValidPW('111122')
