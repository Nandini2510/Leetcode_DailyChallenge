class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0" or grid[i][j] == "X":
                return
            grid[i][j] = "X"

            # bottom
            dfs(i+1, j)
            # top
            dfs(i - 1, j)
            #right
            dfs(i, j + 1)
            #left
            dfs(i, j - 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res