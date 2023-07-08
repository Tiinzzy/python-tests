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

    def find_first_parent(self, node):
        return self._traverse_parent_nodes(self.root, node)

    @staticmethod
    def add_sibling(parent, new_child):
        child = Node(new_child)
        parent.children.append(child)
        return True

    def _traverse_parent_nodes(self, current_node, target_node, parent_node=None):
        if current_node.name == target_node:
            return parent_node
        else:
            for child in current_node.children:
                result = self._traverse_parent_nodes(child, target_node, current_node)
                if result is not None:
                    return result
        return None

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
        even_odd = self._check_odd_even(depth)
        blank = '' if depth < 2 else ' ' * (depth - 2)
        print(blank + '+-' + node.name)
        # if depth == 2:
        #     print('|--', end='')
        #     print(node.name)
        # elif depth > 2:
        #     if even_odd == 'odd':
        #         print(' ' * 2, '|--' * (depth - 2), end='')
        #         print(node.name)
        #     else:
        #         print(' ' * 2, '|--' * (depth - 2), end='')
        #         print(node.name)

        for child in node.children:
            new_depth = depth + 1
            self._print_node(child, new_depth)

    @staticmethod
    def _check_odd_even(number):
        if number % 2 == 0:
            return "even"
        else:
            return "odd"
