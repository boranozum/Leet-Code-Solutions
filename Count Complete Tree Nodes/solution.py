# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:

        if root is None:
            return 0

        height = self.findHeight(root)
        total_nodes = 1
        if height == 0:
            return 1

        if height >= 2:
            total_nodes = int((1 - 2 ** height) / (-1))

        max_level = height + 1

        leaves, _ = self.helper(root, 0, 1, max_level)

        print(f'total_nodes: {total_nodes} - leaves: {leaves} - max_level: {max_level}')

        return total_nodes + leaves

    def helper(self, root: TreeNode, leaf_count: int, level: int, max_level: int) -> (int, bool):

        if root.left is not None:
            if root.right is None:
                return leaf_count + 1, False

            leaf_count, isFull = self.helper(root.left, leaf_count, level + 1, max_level)
            if isFull:
                leaf_count, isFull = self.helper(root.right, leaf_count, level + 1, max_level)

            return leaf_count, True

        if level == max_level:
            return leaf_count + 1, True
        return leaf_count, False

    def findHeight(self, root: TreeNode) -> int:

        if root.left is None:
            return 0

        return 1 + self.findHeight(root.left)







