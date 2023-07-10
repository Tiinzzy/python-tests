import unittest
from binary_tree.binary_tree import BinaryTree


class BinaryTreeTests(unittest.TestCase):

    def test_insert_single_node(self):
        br_tree = BinaryTree()

        br_tree.insert(5)
        self.assertEqual(br_tree.root.weight, 5)
        self.assertIsNone(br_tree.root.left)
        self.assertIsNone(br_tree.root.right)

    def test_insert_multiple_nodes(self):
        br_tree = BinaryTree()

        br_tree.insert(5)
        br_tree.insert(3)
        br_tree.insert(7)
        br_tree.insert(4)
        br_tree.insert(6)

        root = br_tree.root
        self.assertEqual(root.weight, 5)
        self.assertEqual(root.left.weight, 3)
        self.assertEqual(root.right.weight, 7)
        self.assertEqual(root.left.right.weight, 4)
        self.assertEqual(root.right.left.weight, 6)

    def test_show(self):
        br_tree = BinaryTree()

        br_tree.insert(5)
        br_tree.insert(3)
        br_tree.insert(7)
        br_tree.insert(4)
        br_tree.insert(6)

        display = br_tree.show()

        self.assertEqual(br_tree.show(), display)

    def test_node_exist(self):
        br_tree = BinaryTree()

        br_tree.insert(5)
        br_tree.insert(3)
        br_tree.insert(7)

        self.assertTrue(br_tree.node_exist(5))
        self.assertTrue(br_tree.node_exist(3))
        self.assertTrue(br_tree.node_exist(7))
        self.assertFalse(br_tree.node_exist(2))
        self.assertFalse(br_tree.node_exist(8))
        self.assertFalse(br_tree.node_exist(6))

    def test_find_node(self):
        br_tree = BinaryTree()

        br_tree.insert(5)
        br_tree.insert(3)
        br_tree.insert(7)

        node = br_tree._find_node(br_tree.root, 5)
        self.assertEqual(node.weight, 5)
        self.assertIsNone(br_tree._find_node(br_tree.root, 2))
        self.assertIsNone(br_tree._find_node(br_tree.root, 8))
        self.assertIsNone(br_tree._find_node(br_tree.root, 6))

    def test_find_node(self):
        br_tree = BinaryTree()

        br_tree.insert(5)
        br_tree.insert(3)
        br_tree.insert(7)

        node = br_tree._find_node(br_tree.root, 5)
        self.assertEqual(node.weight, 5)
        self.assertIsNone(br_tree._find_node(br_tree.root, 2))
        self.assertIsNone(br_tree._find_node(br_tree.root, 8))
        self.assertIsNone(br_tree._find_node(br_tree.root, 6))
