class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) <= 1:
            return False
        else:
            for i in range(1, len(nums)):
                if (nums[i] == nums[i-1]):
                    return True
                number = nums[i]
            return False

        