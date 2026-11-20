class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #*haven't done the optimal solution yet
        numberFreqMatching = {}
        for n in nums:
            if n not in numberFreqMatching:
                numberFreqMatching[n] = 1
            else: 
                numberFreqMatching[n] += 1

        keys = sorted(numberFreqMatching, key=numberFreqMatching.get, reverse=True)

        top_keys = []
        for i in range(k):
            top_keys.append(keys[i])

        return top_keys
        