class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertBST(self, root, val):
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertBST(root.left, val)
        else:
            root.right = self.insertBST(root.right, val)

        return root


root = None
root = Solution().insertBST(root, 6)
print("Inserted 6")