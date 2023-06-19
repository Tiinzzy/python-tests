
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