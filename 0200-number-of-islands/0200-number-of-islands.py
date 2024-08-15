class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            q = deque()
            q.append((i,j))
            grid[i][j] = "0"

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1, 0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                        q.append((r,c))
                        grid[r][c] = "0"
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i, j)
        return res