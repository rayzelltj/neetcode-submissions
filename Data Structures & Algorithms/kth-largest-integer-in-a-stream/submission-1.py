class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.h = []
        for x in self.nums:
            heapq.heappush(self.h,x)
            if len(self.h) > self.k:
                heapq.heappop(self.h)
        

    def add(self, val: int) -> int:
        #with HELP
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        
        return self.h[0]
        
