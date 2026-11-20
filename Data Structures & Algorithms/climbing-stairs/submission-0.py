class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [None]*(n+1)
        #base case
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else: 
            ways[1] = 1
            ways[2] = 2
            for i in range(3, n+1):
                ways[i] = ways[i-1] + ways[i-2]
        return ways[n]
        
        