class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        h = []
        self.nums.append(val)
        for x in self.nums:
            heapq.heappush(h,x)
            if len(h) > self.k:
                heapq.heappop(h)
        return h[0]
        
