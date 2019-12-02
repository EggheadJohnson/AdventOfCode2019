class intCodeComputer:
    def __init__(self, operations):
        self.operations = map(int, operations.split(','))
        self.error = None
        self.counter = 0
    def run(self):
        continueRunning = True
        while continueRunning:
            # self.printOperations()
            continueRunning = self.nextAction()
        if self.error:
            print self.error
            return False
        else:
            return self.operations[0]
    def nextAction(self):
        action = self.operations[self.counter]
        # print action
        if action == 1:
            # print "adding"
            self.add()
            self.counter += 4
            return True
        elif action == 2:
            # print "multiplying"
            self.mult()
            self.counter += 4
            return True
        elif action == 99:
            return self.end()
        else:
            return self.invalidOpCode()
    def add(self):
        a = self.operations[self.counter+1]
        b = self.operations[self.counter+2]
        destination = self.operations[self.counter+3]
        self.operations[destination] = self.operations[a] + self.operations[b]
    def mult(self):
        a = self.operations[self.counter+1]
        b = self.operations[self.counter+2]
        destination = self.operations[self.counter+3]
        self.operations[destination] = self.operations[a] * self.operations[b]
    def end(self):
        return False
    def invalidOpCode(self):
        self.error = "Invalid opcode " + str(self.operations[self.counter])
        return False
    def printOperations(self):
        print self.operations
