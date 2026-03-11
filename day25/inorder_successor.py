class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        successor = None

        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)

node = root.left  

succ = Solution().inorderSuccessor(root, node)

print("\nInorder Successor of", node.val, ":", succ.val if succ else None)