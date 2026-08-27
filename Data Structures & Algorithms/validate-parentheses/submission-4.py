class Solution:
    def isValid(self, s: str) -> bool:
        last = ""
        from collections import deque
        stack = deque()
        for c in s: 
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) < 1: 
                    return False
                else:
                    last = stack[-1]
                if last == "(": 
                    if c != ")": return False
                elif last == "{": 
                    if c != "}": return False
                elif last == "[":
                    if c != "]": return False
                stack.pop()
        return True if len(stack) == 0 else False
            