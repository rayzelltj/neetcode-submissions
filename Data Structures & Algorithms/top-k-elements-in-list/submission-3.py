class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = count[nums[i]] + 1
            else:
                count[nums[i]] = 1
        key = sorted(count, key = count.get, reverse = True)
        result = []
        for j in range(k):
            result.append(key[j])
        return result


