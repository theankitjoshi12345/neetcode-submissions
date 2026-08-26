class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        ret = []

        for i in range(len(nums)):
            n = nums[i]
            if n not in dict:
                dict[n] = [1, n]
            else:
                dict[n][0] += 1

        values = sorted(list(dict.values()), key = lambda item : item[0], reverse=True)

        for i in range(k):
            ret.append(values[i][1])
        
        return ret
            

