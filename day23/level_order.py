class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Level Order:", Solution().levelOrder(root))