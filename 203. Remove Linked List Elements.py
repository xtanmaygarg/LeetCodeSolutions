# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        List = ListNode("-1")
        List.next = head
        Curr = List
        while(Curr):
            if Curr.next and Curr.next.val == val:
                Curr.next = Curr.next.next
            else:
                Curr = Curr.next
        return List.next
