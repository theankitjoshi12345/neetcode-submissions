# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None:
            newHead = ListNode(head.val, None) 
            head = head.next
        else:
            return None
        while head != None: 
            temp = ListNode(head.val, newHead)
            newHead = temp

            head = head.next

        return newHead

