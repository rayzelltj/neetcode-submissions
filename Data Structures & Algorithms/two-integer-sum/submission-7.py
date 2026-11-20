class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force, O(n^2) -> is my partner somewhere later in the list
        # l = []
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             l.append(i)
        #             l.append(j)
        #             return l
        # return l

        # is my partner somewhere earlier in the list? 
        seen = {}
        seen[nums[0]] = 0
        for i in range(1, len(nums)):
            need = target - nums[i]
            if (need in seen):
                return [seen[need], i]
            seen[nums[i]] = i
        return []

