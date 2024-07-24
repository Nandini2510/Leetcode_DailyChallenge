class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        

        def dfs(i, j, m, n):
            nonlocal num
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 0
            num += 1

            dfs(i + 1, j, m, n)
            dfs(i - 1, j, m, n)
            dfs(i, j + 1, m, n)
            dfs(i, j - 1, m, n)

        
        for i in range(m):
            for j in range(n):
                num = 0
                if grid[i][j] == 1:
                    dfs(i, j, m, n)
                    res = max(res, num)
        return res

                    