# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        Curr = head
        Slow = head
        while(Curr.next):
            if n > 0:
                n -= 1
            else:
                Slow = Slow.next
            Curr = Curr.next
        if head == Slow:
            if n == 0:
                Slow.next = Slow.next.next
            else:
                return head.next
        elif Slow.next:
            Slow.next = Slow.next.next
        else:
            Slow.next = None
        return head
