class intCodeComputer:
    def __init__(self, operations, first_input = None, debugMode = False):
        self.operations = map(int, operations.split(','))
        self.error = None
        self.counter = 0
        self.debugMode = debugMode
        self.array_of_inputs = []
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
            print action, self.counter
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
            self.counter += 2
            return self.pause_on_output
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
        elif action == 99:
            return self.end()
        else:
            return self.invalidOpCode()
    def add(self, modes):
        a = self.operations[self.counter+1]
        b = self.operations[self.counter+2]
        destination = self.operations[self.counter+3]
        if modes[0] == 0:
            a = self.operations[a]
        if modes[1] == 0:
            b = self.operations[b]
        # if modes[2] == 0:
        #     destination = self.operations[destination]
        self.operations[destination] = a + b
    def mult(self, modes):
        a = self.operations[self.counter+1]
        b = self.operations[self.counter+2]
        destination = self.operations[self.counter+3]
        if modes[0] == 0:
            a = self.operations[a]
        if modes[1] == 0:
            b = self.operations[b]
        # if modes[2] == 0:
        #     destination = self.operations[destination]
        self.operations[destination] = a * b
    def storeInput(self, modes):
        # print self.array_of_inputs
        if not self.array_of_inputs:
            userInput = input("Holding for user input: ")
        else:
            userInput = self.array_of_inputs.pop(0)
        destination = self.operations[self.counter+1]
        # if modes[0] == 0:
        #     destination = self.operations[destination]
        self.operations[destination] = userInput
    def retrieveValue(self, modes):
        destination = self.operations[self.counter+1]
        if modes[0] == 0:
            destination = self.operations[destination]
        self.output = destination
        # print destination
    def jumpIfTrue(self, modes):
        boolValue = self.operations[self.counter+1]
        jumpValue = self.operations[self.counter+2]
        if modes[0] == 0:
            boolValue = self.operations[boolValue]
        if modes[1] == 0:
            jumpValue = self.operations[jumpValue]
        if boolValue != 0:
            self.counter = jumpValue
        else:
            self.counter += 3
    def jumpIfFalse(self, modes):
        boolValue = self.operations[self.counter+1]
        jumpValue = self.operations[self.counter+2]
        if modes[0] == 0:
            boolValue = self.operations[boolValue]
        if modes[1] == 0:
            jumpValue = self.operations[jumpValue]
        if boolValue == 0:
            self.counter = jumpValue
        else:
            self.counter += 3
    def lessThan(self, modes):
        a = self.operations[self.counter+1]
        b = self.operations[self.counter+2]
        destination = self.operations[self.counter+3]
        # print a, b, destination
        if modes[0] == 0:
            a = self.operations[a]
        if modes[1] == 0:
            b = self.operations[b]
        # if modes[2] == 0:
        #     destination = self.operations[destination]
        # print a, b, destination
        self.operations[destination] = int(a < b)
    def equals(self, modes):
        a = self.operations[self.counter+1]
        b = self.operations[self.counter+2]
        destination = self.operations[self.counter+3]
        if modes[0] == 0:
            a = self.operations[a]
        if modes[1] == 0:
            b = self.operations[b]
        # if modes[2] == 0:
        #     destination = self.operations[destination]
        self.operations[destination] = int(a == b)
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
