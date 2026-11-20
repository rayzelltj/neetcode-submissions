class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # time complexity
        m, n = len(matrix), len(matrix[0])
        longest = 0
        dp = [[0] * n for _ in range(m)]

        def dfs(r: int, c: int) -> int:
            if dp[r][c] != 0:
                return dp[r][c]
            path = 1

            #top: matrix[r-1][c]
            if r > 0:
                if matrix[r-1][c] > matrix[r][c]:
                    path = max(path, 1 + dfs(r-1, c))
            #bottom
            if r+1 < len(matrix):
                if matrix[r+1][c] > matrix[r][c]:
                    path = max(path, 1 + dfs(r+1, c))
            #left
            if c > 0:
                if matrix[r][c-1] > matrix[r][c]:
                    path = max(path, 1 + dfs(r, c-1))
            #right
            if c+1 < len(matrix[0]):
                if matrix[r][c+1] > matrix[r][c]:
                    path = max(path, 1 + dfs(r, c+1))
            dp[r][c] = path
            return path

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest = max(longest, dfs(i, j))
        return longest