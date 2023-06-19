class CircularQue:
    def __init__(self, capacity):
        self.queue = list(range(capacity))
        self.capacity = capacity
        self.currentLength = 0
        self.front = -1
        self.rear = -1

    def isFull(self):
        return self.capacity == self.currentLength

    def isEmpty(self):
        return self.currentLength == 0

    def add(self, element):
        if self.isFull == False:
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
            i = None
            string = ''
            #Have to figure it out                 