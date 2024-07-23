class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j, m, n):
            if i < 0 or i >= m or j < 0 or j >=n or grid[i][j] != "1":
                return
            grid[i][j] = "*"

            dfs(i+1, j, m, n)
            dfs(i-1, j, m, n)
            dfs(i, j + 1, m, n)
            dfs(i, j - 1, m, n)


        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j,m,n)
        return res

