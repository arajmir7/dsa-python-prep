class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# Create a sample BST
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))

node = Solution().searchBST(root, 7)
print("Search Result:", node.val if node else None)