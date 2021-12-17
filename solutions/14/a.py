import os, collections

file_path = os.path.dirname(os.path.realpath(__file__))

input_path = file_path + "/a.in.txt"

inpt = open(input_path, 'r')

class Reaction:
    def __init__(self, line):
        self.result_chemical = line[1][1]
        self.result_amount = line[1][0]
        self.reagents = {}
        for chemical in line[0]:
            self.reagents[chemical[1]] = chemical[0]
    def printReaction(self):
        printing_line = ''
        for chemical in self.reagents:
            printing_line += str(self.reagents[chemical]) + ' ' + chemical + ', '
        printing_line = printing_line[:-2]
        printing_line += ' => '
        printing_line += str(self.result_amount) + ' ' + self.result_chemical
        return printing_line

def parseLine(line):
    left, right = line.split(' => ')
    left = left.split(', ')
    right_amount, right_substance = right.split(' ')
    right_amount = int(right_amount)

    left = map(lambda entry: ( int(entry.split(' ')[0]), entry.split(' ')[1]), left)

    return left, (right_amount, right_substance)

def parseAllLinesFromInpt(inpt):
    result_map = {}
    for line in inpt:
        line = parseLine(line)
        reaction = Reaction(line)
        # reaction.printReaction()
        result_map[reaction.result_chemical] = reaction
    return result_map

def constructFullReaction(result_map):
    production_queue = collections.deque()
    fuel_step = {
        'key': 'FUEL',
        'amt': result_map['FUEL'].result_amount,
        'reagents': reagents
    }
    production_queue.append(fuel_step)

    used = {}
    produced = {}

    while production_queue:
        current_step = production_queue.popleft()
        for reagent, amt in current_step['reagents'].items:
            production_queue.append({
                'key': reagent,
                'amt': amt,
                'reagents': result_map[reagent].reagents
            })
        produced.append


result_map = parseAllLinesFromInpt(inpt)
for c in result_map:
    print c, result_map[c].printReaction()
