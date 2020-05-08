# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        Current = head
        Next = head.next
        DoubleNext = Next.next
        Current.next = None
        while(True):
            Next.next = Current
            Current = Next
            Next = DoubleNext
            if not Next:
                return Current
            DoubleNext = DoubleNext.next
            if not DoubleNext:
                Next.next = Current
                return Next

# Short Version
class Solution(object):        
    def reverseList(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
