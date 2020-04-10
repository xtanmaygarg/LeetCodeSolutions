# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        Answer = Current = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                Current.next = l1
                l1 = l1.next
            else:
                Current.next = l2
                l2 = l2.next
            Current = Current.next
        
        if l1:
            Current.next = l1
        else:
            Current.next = l2

        return Answer.next
