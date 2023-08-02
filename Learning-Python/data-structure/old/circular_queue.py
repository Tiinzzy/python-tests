class CircularQue:
    def __init__(self, capacity):
        self.queue = list(range(capacity))
        self.capacity = capacity
        self.currentLength = 0
        self.front = -1
        self.rear = -1

    def isFull(self):
        print(self.capacity,'<<< capacity')
        print(self.currentLength,'<<< current length')
        return self.capacity == self.currentLength

    def isEmpty(self):
        return self.currentLength == 0

    def add(self, element):
        if self.isFull is not False:
            self.rear = (self.rear+1) % self.capacity
            self.rear = self.rear+1
            self.queue[self.rear] = element
            self.currentLength += 1
            if self.front == -1:
                self.front = self.rear

    def remove(self):
        if self.isEmpty == True:
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front+1) % self.capacity
        self.front = self.front + 1
        self.currentLength -= 1
        if self.isEmpty == True:
            self.rear = -1
            self.front = -1
        return item

    def peack(self):
        if self.isEmpty == False:
            return self.queue[self.front]
        elif self.isEmpty == True:
            return None

    def print(self):
        if self.isEmpty:
            print('Queue is empty')
        else:
            i = self.front
            string = ''

            while i != self.rear:
                i = (i + 1) % self.capacity
                string += self.queue[i] + " "
            string +=  self.queue[i]
            print(string)