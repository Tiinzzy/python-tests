class Node:
    def __init__(self, payload):
        self.payload = payload
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

    def show(self):
        print(self.payload, '->', ('None' if self.next is None else self.next.payload))

    def show_chain(self):
        start = self
        next_node_exist = True
        chain = ''
        while next_node_exist:
            chain += str(start.payload)
            if start.next is not None:
                start = start.next
                chain += ' -> '
            else:
                next_node_exist = False
                chain += ' -> None'
        print(chain)


class OneDirectionLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        size = 0
        start = self.head
        if start is not None:
            size = 1
            while start.next is not None:
                start = start.next
                size += 1
        return size

    def describe(self):
        print('head:', self.head.payload if self.head is not None else 'None')
        print('tail:', self.tail.payload if self.tail is not None else 'None')
        print('size:', self.size())
        if self.head is not None:
            self.head.show_chain()
        print('----------------------------')

    def add_to_tail(self, payload):
        n = Node(payload)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def add_to_head(self, payload):
        n = Node(payload)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n

    def remove_from_tail(self):
        if self.head is None:
            return None
        else:
            result = self.tail
            new_tail = self.head
            if new_tail is not None:
                while new_tail.next != self.tail:
                    new_tail = new_tail.next
            new_tail.next = None
            self.tail = new_tail
            return result

    def remove_from_head(self):
        if self.head is None:
            return None
        else:
            result = self.head
            self.head = result.next
            if self.head is None:
                self.tail = None
            return result

    def payload_exist(self, payload):
        if self.head is None:
            return False
        else:
            start = self.head
            while start.next is not None and start.payload != payload:
                start = start.next
            return start if start.payload == payload else None

    def remove_payload(self, payload):
        pass
