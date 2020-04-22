# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        Next = head
        DoubleNext = head
        while(DoubleNext and DoubleNext.next):
            Next = Next.next
            DoubleNext = DoubleNext.next.next
        return Next
        
