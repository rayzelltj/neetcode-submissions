class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ## time complexity: O(n!)
        ## space complexity: O(n)
        result = []

        def backtrack(permute: List[int]):
            if len(permute) == len(nums):
                result.append(permute[:])
            
            for n in nums:
                if n in permute:
                    continue
                permute.append(n)
                backtrack(permute)
                permute.pop()

        backtrack([])
        return result

