import unittest
from src.lab3 import Sl
from src.lab3 import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def test_balanced_tree(self):
        root1 = BinaryTree(1)
        root1.left = BinaryTree(2)
        root1.right = BinaryTree(3)
        root1.left.left = BinaryTree(4)
        root1.left.right = BinaryTree(5)
        solution = Sl()
        self.assertTrue(solution.is_tree_balanced(root1))

    def test_unbalanced_tree(self):
        root2 = BinaryTree(1)
        root2.left = BinaryTree(2)
        root2.right = BinaryTree(3)
        root2.left.left = BinaryTree(4)
        root2.left.right = BinaryTree(5)
        root2.left.left.left = BinaryTree(6)
        solution = Sl()
        self.assertFalse(solution.is_tree_balanced(root2))

    def test_single_node_tree(self):
        root3 = BinaryTree(1)
        solution = Sl()
        self.assertTrue(solution.is_tree_balanced(root3))

    def test_empty_tree(self):
        root4 = None
        solution = Sl()
        self.assertTrue(solution.is_tree_balanced(root4))


if __name__ == '__main__':
    unittest.main()
