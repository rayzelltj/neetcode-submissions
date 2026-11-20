class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = [None] * (len(nums))
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        houses[0] = nums[0]
        houses[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            houses[i] = max(houses[i-1], nums[i] + houses[i-2])
        return max(houses[len(nums)-1], houses[len(nums)-2])



        