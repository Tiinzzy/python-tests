class BdNode:
    def __init__(self, payload):
        self.payload = payload
        self.next = None
        self.prev = None


class BiDirectionLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def describe(self):
        print('---------------------------->>')
        print('head:', self.head.payload if self.head is not None else 'None')
        print('tail:', self.tail.payload if self.tail is not None else 'None')
        print('size:', self.size)
        print('<<----------------------------')

    def show_chain(self):
        start = self.head
        next_node_exist = True
        chain = ''
        while next_node_exist:
            chain += str(start.payload)
            if start.next is not None:
                start = start.next
                chain += ' <-> '
            else:
                next_node_exist = False
                chain += ' -> None'
        print(chain)

    def add_to_tail(self, payload):
        if self.head is None:
            n = BdNode(payload)
            self.head = n
            self.tail = n
        else:
            n = BdNode(payload)
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.size += 1

    def add_to_head(self, payload):
        if self.head is None:
            n = BdNode(payload)
            self.head = n
            self.tail = n
        else:
            n = BdNode(payload)
            n.next = self.head
            self.head.prev = n
            self.head = n
        self.size += 1

    def add_to_middle(self, payload, index):
        if index < 0 or index >= self.size:
            return False
        elif index == 0:
            self.add_to_head(payload)
            return True
        elif index == self.size:
            self.add_to_tail(payload)
            return True
        else:
            next_node_pointer = self.head
            for i in range(index):
                next_node_pointer = next_node_pointer.next
            print(next_node_pointer.payload)
            n = BdNode(payload)
            n.next = next_node_pointer
            n.prev = next_node_pointer.prev
            n.next.prev = n
            n.prev.next = n
            self.size += 1
            return True

    def show_list(self):
        self.show_chain()

    def remove_from_tail(self):
        if self.head is None:
            return None
        else:
            result = self.tail
            new_tail = self.head
            if new_tail is not None:
                while new_tail.next is not None and new_tail.next != self.tail:
                    new_tail = new_tail.next
            if new_tail.next is None:
                self.tail = None
                self.head = None
            else:
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

    def remove_from_middle(self, payload):
        if self.head is None:
            return None
        elif self.head.payload == payload:
            self.remove_from_head()
        elif self.tail.payload == payload:
            self.remove_from_tail()
        else:
            next_node_pointer = self.head
            for i in range(self.size):
                while next_node_pointer is not None:
                    print(next_node_pointer.payload)
                    if next_node_pointer.payload == payload:
                        next_node_pointer.prev.next = next_node_pointer.next
                        next_node_pointer.next.prev = next_node_pointer.prev
                    next_node_pointer = next_node_pointer.next
