class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberFreqMatching = {}
        sortedNums = sorted(nums)
        for n in nums:
            if n not in numberFreqMatching:
                numberFreqMatching[n] = 1
            else: 
                numberFreqMatching[n] += 1
        top_keys = heapq.nlargest(k, numberFreqMatching, key=numberFreqMatching.get)
        return top_keys
        