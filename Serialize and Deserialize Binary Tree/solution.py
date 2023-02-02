# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = ""

        return self.serialize_helper(root, result, 1)

    def serialize_helper(self, root: TreeNode, serialized_string, level):

        if root is None:
            return "-"

        s = str(root.val)
        s_left = self.serialize_helper(root.left, serialized_string,level+1)
        s_right = self.serialize_helper(root.right, serialized_string,level+1)

        serialized_string += s + s_left + s_right

        return serialized_string


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        root, _ = self.deserialize_helper(data)

        return root


    def deserialize_helper(self, data):

        if data[0] == "-":
            data = data[1:]
            return None, data

        root = TreeNode(int(data[0]))
        root.left, data = self.deserialize_helper(data[1:])
        root.right, data = self.deserialize_helper(data)

        return root, data








# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
ans = Codec().deserialize(Codec().serialize(root))
print(ans.val)