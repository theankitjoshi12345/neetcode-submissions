class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in dict:
                dict[sortedS] = [s]
            else:               
                dict[sortedS].append(s)

        return list(dict.values())