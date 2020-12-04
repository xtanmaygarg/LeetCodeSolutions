# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        Curr = head
        if Curr.next and Curr.val == Curr.next.val:
            Num = Curr.val
            while(Curr and Curr.val == Num):
                Curr = Curr.next
            head = Curr
        
        if not head:
            return head
        
        if Curr.next and Curr.val == Curr.next.val:
            head = self.deleteDuplicates(Curr)
        else:
            Curr.next = self.deleteDuplicates(Curr.next)
        return head
