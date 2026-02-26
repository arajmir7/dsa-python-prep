class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

def printMiddle(node):
    if node:
        print("Middle node value:", node.val)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
mid = sol.middleNode(head)

printMiddle(mid)