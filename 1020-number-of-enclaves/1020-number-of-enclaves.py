class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(i, j, m, n):
            if i < 0 or i >=m or j < 0 or j >=n or grid[i][j] != 1:
                return
            grid[i][j] = 2
            dfs(i + 1, j, m, n)
            dfs(i - 1, j, m, n)
            dfs(i, j + 1, m, n)
            dfs(i, j - 1, m, n)
        
        for i in range(m):
            for j in range(n):
                if (i ==0 or j == 0 or i == m or j == n):
                    dfs(i, j, m, n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 1
        return ans
        