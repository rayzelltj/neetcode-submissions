class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index: int, l: List[int]) -> None:
            s = sum(l)
            if s == target:
                result.append(l[:])
                return

            for i in range(index, len(nums)):
                if (s + nums[i]) > target:
                    continue
                l.append(nums[i])
                backtrack(i, l)
                l.pop()

        backtrack(0, [])
        return result