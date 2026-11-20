class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(m * n)
        m = len(grid)
        n = len(grid[0])
        result = 0
        #dfs -> how wide/far this island spans
        #is a complete island if there are no more unseen adj 1s
        def dfs(r: int, c: int):
            if (r<0 or c < 0 or r >=m or c >=n or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r,c -1)
            dfs(r, c+1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    result = result + 1
                    dfs(r,c)
    
        return result


