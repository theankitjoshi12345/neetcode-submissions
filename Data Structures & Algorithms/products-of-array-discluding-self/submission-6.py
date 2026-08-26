class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from math import prod
        total = math.prod(nums)

        return [int(total/nums[i]) if nums[i] != 0 else (prod(nums[0:i]) if not None else 1) * (prod(nums[i+1:]) if not None else 1) for i in range(len(nums))]
