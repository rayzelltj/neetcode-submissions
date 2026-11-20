class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if a number is already part of a sequence, it cannot form a new sequence
        # * had help...
        longest = 0
        numSet = set(nums) # looking at set, removes duplicates
        for num in numSet:  
            if num - 1 not in numSet: #looking at if we should start from here or not
                count = 1
                current = num
                while current + 1 in numSet:
                    current += 1
                    count += 1
                longest = max(longest, count)
        return longest

            
        