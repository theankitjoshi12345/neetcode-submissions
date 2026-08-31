class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ret = []

        for i in range(len(nums)- 1):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            a = nums[i]
            # first number > 0 in sorter array means sum cannot make it to 0
            if a > 0:
                break 
            l = i + 1
            r = len(nums) - 1

            while l < r: 
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0: 
                    l += 1
                elif threeSum > 0: 
                    r -= 1
                elif threeSum == 0: 
                    ret.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ret