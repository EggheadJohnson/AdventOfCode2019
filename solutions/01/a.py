import os

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

tot = 0

for i in inpt:
    tot += int(i)/3 - 2

print tot, tot/3

print tot/3 - 2
