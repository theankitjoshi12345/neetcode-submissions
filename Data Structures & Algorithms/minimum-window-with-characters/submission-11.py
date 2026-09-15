class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        have, need = 0, 0

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        need = len(countT)

        l = 0
        resLen = float("infinity")
        res = [-1, -1]

        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:

                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                c = s[l]
                if c in countT:

                    window[c] -= 1
                    if window[c] < countT[c]:
                        have -=1

                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""



