class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head.next.next.next.next.next = head.next.next

sol = Solution()
print("Cycle detected:", sol.hasCycle(head))