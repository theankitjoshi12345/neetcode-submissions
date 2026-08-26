class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += (str(len(s)))
            ret += ("#")
            ret += (s)
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        leng, i = 0, 0
        while i < len(s):
            if s[i].isdigit():
                leng = leng * 10 + int(s[i])
            else:
                ret.append(s[i + 1 : i + 1 + leng])
                i = i + leng
                leng = 0
            i += 1
        
        return ret

