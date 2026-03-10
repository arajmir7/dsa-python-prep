class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):

        def helper(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root, float('-inf'), float('inf'))


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

print("Valid BST:", Solution().isValidBST(root))