class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0: # first number >0 → can't sum to 0
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L, R = i + 1, len(nums) - 1
            while L < R: 
                threeSum = nums[i] + nums[R] + nums[L]
                if (threeSum < 0):
                    L = L + 1
                elif (threeSum > 0):
                    R = R - 1
                else: 
                    ans.append([nums[i], nums[R], nums[L]])
                    L = L + 1
                    while L < R and nums[L] == nums[L - 1]:
                        L = L + 1
        return ans
        