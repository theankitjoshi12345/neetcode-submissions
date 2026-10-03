class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        multiplier = 1
        while l1:
            # Multiply the digit by its place value (1s, 10s, 100s...)
            num1 = num1 + l1.val * multiplier
            multiplier *= 10
            l1 = l1.next
        
        num2 = 0
        multiplier = 1
        while l2: 
            num2 = num2 + l2.val * multiplier
            multiplier *= 10
            l2 = l2.next

        # Since LeetCode expects the output reversed (ones digit first),
        # we read the string from left to right (no reversed() needed!)
        head = ListNode()
        ret = head
        for digit in str(num1 + num2)[::-1]:  # Using your preferred reverse slice
            head.next = ListNode(int(digit), None)
            head = head.next

        return ret.next
