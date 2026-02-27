class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next

def createList(arr):
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

arr1 = list(map(int, input("Enter sorted list 1: ").split()))
arr2 = list(map(int, input("Enter sorted list 2: ").split()))

l1 = createList(arr1)
l2 = createList(arr2)

sol = Solution()
merged = sol.mergeTwoLists(l1, l2)

print("Merged List:")
printList(merged)