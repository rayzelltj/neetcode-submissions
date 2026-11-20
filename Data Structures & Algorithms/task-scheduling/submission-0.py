class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #each task 1 unit time
        # minimize idle time
        # HAD HELP!!!!!
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        
        q = deque() #pair of [-cnt, idleTime]

        while maxHeap or q:
            time = time + 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # add 1 cuz the count is negative
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

