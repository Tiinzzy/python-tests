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
            # last_node = self.tail
            # last_node.next = node
            # self.tail = node
            # self.tail.previous = last_node
            # self.size += 1

            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.size += 1
            return True
        else:
            if index < 0 or index > self.size:
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

    def remove(self, index=None):
        if index is None:
            last_node = self.tail
            self.tail = last_node.previous
            self.tail.next = None
            # remove from tail
            self.size -= 1
            return last_node.payload
        else:
            if index < 0 or index > self.size:
                return False
            elif index == 0:
                first_node = self.head
                self.head = first_node.next
                self.size -= 1
                return first_node.payload
            else:
                node_pointer = self.head
                for i in range(self.size):
                    if i == index:
                        node_pointer.previous.next = node_pointer.next
                        node_pointer.next.previous = node_pointer.previous
                        self.size -= 1
                        return node_pointer.payload
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
                for i in range(self.size):
                    if i == index:
                        node = node_pointer
                        return node_pointer.payload
                    node_pointer = node_pointer.next
