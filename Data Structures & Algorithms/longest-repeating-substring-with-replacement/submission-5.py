class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        replacements = 0
        longest = 0
        for l in range(len(s)):
            if l > 0 and s[l] == s[l-1]:
                continue
            r = l 
            while s[l] == s[r] or replacements < k: 
                if s[l] != s[r]:
                    replacements += 1
                r += 1
                if not r < len(s):
                    break

            while replacements < k and l > 0: 
                l -= 1
                replacements += 1

            longest = max(longest, r - l)
            replacements = 0

        return longest