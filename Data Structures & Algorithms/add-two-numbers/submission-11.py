# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1, num2, multiplier = 0, 0, 1
        while l1 and l2:
            num1, num2, multiplier = num1 + l1.val * multiplier, num2 + l2.val * multiplier, multiplier * 10
            l1, l2 = l1.next, l2.next

        while l1:
            num1, multiplier = num1 + l1.val * multiplier, multiplier * 10  
            l1 = l1.next

        while l2:
            num2, multiplier = num2 + l2.val * multiplier, multiplier * 10
            l2 = l2.next

        dummy = ListNode(0)
        head = dummy
        for d in str(num1 + num2)[::-1]:
            dummy.next = ListNode(int(d), None)
            dummy = dummy.next

        return head.next
            