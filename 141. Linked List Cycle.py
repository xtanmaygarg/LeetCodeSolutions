# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        Next = head
        DoubleNext = head
        while(DoubleNext and DoubleNext.next):
            Next = Next.next
            DoubleNext = DoubleNext.next.next
            if Next == DoubleNext:
                return True
        return False
        
