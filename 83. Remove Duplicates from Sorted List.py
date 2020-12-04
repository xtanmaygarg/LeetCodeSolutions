# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        Curr = head
        while(Curr):
            if Curr.next and Curr.val == Curr.next.val:
                Curr.next = Curr.next.next
            else:
                Curr = Curr.next
        return head
