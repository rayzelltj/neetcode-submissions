class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = []
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            if numbers[lo] + numbers[hi] == target:
                answer.append(lo+1)
                answer.append(hi+1)
            if numbers[lo] + numbers[hi] < target:
                lo = lo + 1
            else: 
                hi = hi - 1
        return answer

        