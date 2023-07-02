class Node:
    def __init__(self, payload):
        self.payload = payload
        self.next = None
        self.previous = None


class BidirectionalLinkelist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_head(self):
        return self.head.payload

    def get_tail(self):
        return self.tail.payload

    def add(self, payload, index=None):
        node = Node(payload)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return True
        elif index is None:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.size += 1
            return True
        else:
            if index < 0 or index >= self.size:
                return False
            elif index == 0:
                node.next = self.head
                self.head = node
                self.head.next.previous = self.head
                self.size += 1
                return True
            else:
                previous_node = self.head
                for _ in range(index-1):
                    previous_node = previous_node.next
                node.next = previous_node.next
                node.previous = previous_node
                previous_node.next = node
                node.next.previous = node
                self.size += 1
                return True

    def remove_when_size_one(self):
        last_node = self.tail
        self.head = None
        self.tail = None
        self.size = 0
        return last_node

    def remove_from_list(self, node):
        node.next = None
        node.previous = None
        self.size -= 1
        return node.payload

    def remove(self, index=None):
        if self.head is None:
            return None
        elif index is None:
            if self.size == 1:
                return self.remove_when_size_one()
            else:
                last_node = self.tail
                self.tail = last_node.previous
                self.tail.next = None
                return self.remove_from_list(last_node)
        else:
            if index < 0 or index > self.size:
                return None
            elif index == 0:
                if self.size == 1:
                    return self.remove_when_size_one()
                else:
                    first_node = self.head
                    self.head = self.head.next
                    self.head.previous = None
                    return self.remove_from_list(first_node)
            else:
                node_pointer = self.head
                for i in range(self.size):
                    if i == index:
                        node_pointer.previous.next = node_pointer.next
                        node_pointer.next.previous = node_pointer.previous
                        return self.remove_from_list(node_pointer)
                    node_pointer = node_pointer.next

    def show_all(self, reverse=False):
        if reverse:
            node = self.tail
            result = ''
            while node is not None:
                result = ' <-- ' + str(node.payload) + result
                node = node.previous
        else:
            node = self.head
            result = ''
            while node is not None:
                result = result + str(node.payload) + ' --> '
                node = node.next
        print(result)

    def get_element(self, index=None):
        node_pointer = self.head
        if index is None:
            return self.tail.payload
        elif index == 0:
            return self.head.payload
        else:
            if index < 0 or index > self.size:
                return None
            else:
                for _ in range(index):
                    node_pointer = node_pointer.next
                return node_pointer.payload

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def find_first(self, search_function):
        first_not_found = True
        node_pointer = self.head
        while first_not_found and self.size > 0 and node_pointer is not None:
            if search_function(node_pointer.payload):
                return node_pointer.payload
            node_pointer = node_pointer.next
        return None
