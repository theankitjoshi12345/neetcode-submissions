class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c.lower() for c in s if c.isalnum()])
        i, j = 0, len(s) - 1
        for _ in range(len(s)//2):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True