class Node:
    def __init__(self, name):
        self.name = name
        self.children = []


class OrganizationChart:
    def __init__(self):
        self.root = None

    def add_child(self, name, parent=None):
        if parent is None:
            if self.root is None:
                self.root = Node(name)
                return self.root
            else:
                return None
        else:
            child = Node(name)
            parent.children.append(child)
            return child

    def find_first_node(self, name):
        return self._travers_node_until_find(self.root, name)

    def show_org_chart(self):
        self._print_node(self.root, 2)

    def _travers_node_until_find(self, node, name):
        if node.name == name:
            return node
        else:
            for child in node.children:
                result = self._travers_node_until_find(child, name)
                if result is not None:
                    return result
        return None

    def _print_node(self, node, depth):
        if depth >= 2:
            print('--' * (depth - 2), end='')
            print('--+', end=' ')
            print(node.name)
        else:
            print('--' * depth, end='')
            print(node.name)
        for child in node.children:
            new_depth = depth + 1
            self._print_node(child, new_depth)
