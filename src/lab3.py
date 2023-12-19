from typing import Optional


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Sl:
    def is_tree_balanced(self, root: Optional[BinaryTree]) -> bool:
        return self.ds(root)[0]

    def ds(self, root):
        if not root:
            return [True, 0]

        left, right = self.ds(root.left), self.ds(root.right)
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]
