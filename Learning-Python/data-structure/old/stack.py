from one_directional_linked_list import OneDirectionLinkedList


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.od_ll = OneDirectionLinkedList()

    def push(self, payload):
        if self.od_ll.size() < self.max_size:
            self.od_ll.add_to_tail(payload)
            return True
        else:
            return False

    def pop(self):
        n = self.od_ll.remove_from_tail()
        return n.payload if n is not None else None

    def size(self):
        return self.od_ll.size()

    def is_empty(self):
        return self.od_ll.size() == 0
