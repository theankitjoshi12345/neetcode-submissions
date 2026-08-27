class Solution:
    def evalRPN(self, t: List[str]) -> int:
        stack = deque()
        i = 0

        def helper(s: str) -> bool:
            try: 
                int(s)
                return True
            except (ValueError, TypeError):
                return False


        while i < len(t): 
            if helper(t[i]):
                stack.append(int(t[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if t[i] == "+":
                    stack.append(a+b)
                elif t[i] == "-":
                    stack.append(b-a)
                elif t[i] == "/":
                    if (a<0 and b>0) or (a>0 and b<0) :
                        stack.append(-(abs(b)//abs(a)))
                    else:
                        stack.append((abs(b)//abs(a)))
                elif t[i] == "*":
                    stack.append(a*b)
            i += 1
        return stack.pop()