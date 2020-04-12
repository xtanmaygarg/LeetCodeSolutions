# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        Result = ListNode(0)
        Curr = Result
        Carry = 0
        while(l1 and l2):
            S = l1.val + l2.val + Carry
            if S >= 10:
                Curr.next = ListNode(S % 10)
                Carry = 1
            else:
                Curr.next = ListNode(S)
                Carry = 0
            Curr = Curr.next
            l1 = l1.next
            l2 = l2.next
        while(l1):
            Curr.next = ListNode((l1.val + Carry) % 10)
            Carry = (l1.val + Carry) // 10
            l1 = l1.next
            Curr = Curr.next
        while(l2):
            Curr.next = ListNode((l2.val + Carry) % 10)
            Carry = (l2.val + Carry) // 10
            l2 = l2.next
            Curr = Curr.next
        if Carry:
            Curr.next = ListNode(Carry)
        return Result.next
