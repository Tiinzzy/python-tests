
class QueueImpl:
    def __init__(self):
        self.queue = []

    def add(self, element):
        self.queue.append(element)

    def remove(self):
        self.queue.pop(0)

    def isEmpty(self):
        print(self.size == 0)
    
    def size(self):
        print(len(self.queue))

    def peek(self):
        print(self.queue[0])

    def print(self):
        print(self.queue)        


class QueueOptimized:
    def __init__(self):
        self.queue = {}
        self.rear = 0
        self.front = 0

    def add(self, element):
        self.queue[self.rear] = element
        self.rear +=1

    def remove(self):
        item = self.queue[self.front]
        self.queue.pop(self.front)
        self.front +=1
        return item

    def isEmpty(self):
        print(self.rear - self.front == 0)
    
    def size(self):
        print(self.rear - self.front)

    def peek(self):
        print(self.queue[self.front])

    def print(self):
        print(self.queue)  