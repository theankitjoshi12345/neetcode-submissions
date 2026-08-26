class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]].append(i)
            else:
                dict[nums[i]] = [i]

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in dict:
                if not needed == nums[i]:
                    return sorted([dict[needed][0], i])
                elif len(dict[needed]) > 1:
                    return dict[needed][0:2]

        return -1
