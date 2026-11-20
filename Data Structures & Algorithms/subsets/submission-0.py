class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        #index: which # we're currently deciding on,
        #path: current subset being built
        def backtrack(index, path) -> None:
            # base case:
            if index == len(nums):
                result.append(path[:]) # return a copy of list
                return
            
            #Decision 1: include nums[index]
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            #Decision 2: skip nums[index]
            backtrack(index + 1, path)
        backtrack(0, [])
        return result