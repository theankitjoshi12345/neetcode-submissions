class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackI, stackT = stack.pop()
                temperatures[stackI] = i - stackI
            stack.append((i, t))
        while stack:
            stackI, stackT = stack.pop()
            temperatures[stackI] = 0
        return temperatures