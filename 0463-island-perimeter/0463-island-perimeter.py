class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = [0]
        def dfs(i, j, n, m,res):
            if (i < 0 or i >= m) or (j < 0 or j >=n) or grid[i][j] == 0:
                res[0] += 1
                return
            if grid[i][j] == -1:
                return
            grid[i][j] = -1
            dfs(i+1, j, n, m,res)
            dfs(i, j+1, n, m,res)
            dfs(i-1, j, n, m,res)
            dfs(i, j-1, n, m,res)
        
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j,n, m,res)
        return res[0]