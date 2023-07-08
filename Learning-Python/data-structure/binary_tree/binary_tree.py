class Node:
    def __init__(self, weight):
        self.weight = weight
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, weight):
        if self.root is None:
            self.root = Node(weight)
        else:
            self._insert_by_direction(self.root, weight)

    def show(self):
        print('THIS IS ROOT >>', self.root.weight)
        self._show_node(self.root)

    def node_exist(self, w):
        return self._find_node(self.root, w) is not None

    def _insert_by_direction(self, node, w):
        if node.weight < w:
            if node.right is None:
                node.right = Node(w)
                return
            else:
                self._insert_by_direction(node.right, w)
        else:
            if node.left is None:
                node.left = Node(w)
                return
            else:
                self._insert_by_direction(node.left, w)

    def _show_node(self, node):
        if node is None:
            return

        node_str = ' > ' + str(node.weight)
        node_str += ", left: " + ('None' if node.left is None else str(node.left.weight))
        node_str += ", right: " + ('None' if node.right is None else str(node.right.weight))
        # print(node.weight)
        self._show_node(node.right)
        print(node.weight)
        self._show_node(node.left)
        # print(node_str)

    def _find_node(self, node, w):
        if node is None or w is None:
            return None
        elif node.weight == w:
            return node
        elif node.weight < w:
            return self._find_node(node.right, w)
        else:
            return self._find_node(node.left, w)
