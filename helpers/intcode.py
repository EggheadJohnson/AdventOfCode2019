class intCodeComputer:
    def __init__(self, operations, first_input = None, debugMode = False, extend_to = 0):
        self.operations = map(int, operations.split(','))
        self.extendTo(extend_to) # Start with 5000, if it OOB, make it bigger
        self.error = None
        self.counter = 0
        self.debugMode = debugMode
        self.array_of_inputs = []
        self.relative_base = 0
        self.output = None
        if first_input:
            self.array_of_inputs.append(first_input)
        self.stopped = False
    def run(self, array_of_inputs = None, pause_on_output = False):
        if array_of_inputs:
            self.array_of_inputs.extend(array_of_inputs)
        self.pause_on_output = pause_on_output
        self.stopped = False
        continueRunning = True
        while continueRunning:
            if self.debugMode:
                self.printOperations()
            continueRunning = self.nextAction()
        if self.error:
            print self.error
            return False
        else:
            return self.output
    def nextAction(self):
        action, modes = self.parseNextAction()
        if self.debugMode:
            print action, self.counter, modes
        if action == 1:
            # print "adding"
            self.add(modes)
            self.counter += 4
            return True
        elif action == 2:
            # print "multiplying"
            self.mult(modes)
            self.counter += 4
            return True
        elif action == 3:
            self.storeInput(modes)
            self.counter += 2
            return True
        elif action == 4:
            self.retrieveValue(modes)
            print self.output
            self.counter += 2
            return not self.pause_on_output
        elif action == 5:
            self.jumpIfTrue(modes)
            return True
        elif action == 6:
            self.jumpIfFalse(modes)
            return True
        elif action == 7:
            self.lessThan(modes)
            self.counter += 4
            return True
        elif action == 8:
            self.equals(modes)
            self.counter += 4
            return True
        elif action == 9:
            self.adjust_relative_offset()
            self.counter += 2
            return True
        elif action == 99:
            return self.end()
        else:
            return self.invalidOpCode()
    def add(self, modes):
        a, b = self.getParameters(2, modes)

        destination = self.operations[self.counter + 3]

        print modes, a, b, destination

        self.operations[destination] = a + b
    def mult(self, modes):
        a, b = self.getParameters(2, modes)

        destination = self.operations[self.counter + 3]
        self.operations[destination] = a * b
    def storeInput(self, modes):
        if not self.array_of_inputs:
            userInput = input("Holding for user input: ")
        else:
            userInput = self.array_of_inputs.pop(0)
        destination = self.operations[self.counter + 1]
        # if modes[0] == 0:
        #     destination = self.operations[destination]
        self.operations[destination] = userInput
    def retrieveValue(self, modes):
        destination = self.getParameters(1, modes)[0]
        self.output = destination
        # print destination
    def jumpIfTrue(self, modes):
        boolValue, jumpValue = self.getParameters(2, modes)
        if boolValue != 0:
            self.counter = jumpValue
        else:
            self.counter += 3
    def jumpIfFalse(self, modes):
        boolValue, jumpValue = self.getParameters(2, modes)
        if boolValue == 0:
            self.counter = jumpValue
        else:
            self.counter += 3
    def lessThan(self, modes):
        a, b, destination = self.getParameters(3, modes)
        self.operations[destination] = int(a < b)
    def equals(self, modes):
        a, b, destination = self.getParameters(3, modes)
        self.operations[destination] = int(a == b)
    def adjust_relative_offset(self):
        adjustment = self.operations[self.counter + 1]
        self.relative_base += adjustment
    def end(self):
        self.stopped = True
        return False
    def invalidOpCode(self):
        self.error = "Invalid opcode " + str(self.operations[self.counter])
        return False
    def printOperations(self):
        print self.operations
    def parseNextAction(self):
        action = str(self.operations[self.counter])
        action = '0' * (5-len(action)) + action
        code = int(action[-2:])
        modes = map(int, list(action[:3]))
        modes.reverse()
        return code, modes
    def extendTo(self, size):
        while len(self.operations) < size:
            self.operations.append(0)
    def getParameters(self, count, modes):
        # 0 -> index
        # 1 -> literal value
        # 2 -> offset from relative base

        result = []

        for i in range(1, count+1):
            val = self.operations[self.counter + i]
            print val

            if modes[i - 1] == 0:
                val = self.operations[val]
            elif modes[i - 1] == 1:
                pass
            elif modes[i - 1] == 2:
                val = self.operations[val + self.relative_base]
            result.append(val)

        print result
        return result
