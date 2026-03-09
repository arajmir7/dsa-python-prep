class Solution:
    def isBalanced(self, root):

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1
    
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

sol = Solution()
print("Is Balanced:", sol.isBalanced(root))