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

    def remove(self, w):
        if self.root is None:
            return self.root

        # Recursive calls for ancestors of
        # node to be deleted
        if self.root.weight > w:
            self.root.left = self.remove(self.root.left.weight)
        elif self.root.weight < w:
            self.root.right = self.remove(self.root.right.weight)

        if self.root.left is None:
            temp = self.root.right
            self.root = temp
            return temp
        elif self.root.right is None:
            temp = self.root.left
            self.root = temp
            return temp
        else:
            succ_parent = self.root
            succ = self.root.right
            while succ.left is not None:
                succ_parent = succ
                succ = succ.left

            # Delete successor.  Since successor
            # is always left child of its parent
            # we can safely make successor's right
            # right child as left of its parent.
            # If there is no succ, then assign
            # succ.right to succParent.right
            if succ_parent != self.root:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right

            # Copy Successor Data to root
            self.root.key = succ.key

            # Delete Successor and return root
            del succ
            return self.root

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
        print(node_str)
        self._show_node(node.right)
        # print(node.weight)
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
