class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        bfs = deque()
        dist = 0
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    bfs.append((i,j))
                else:
                    mat[i][j] = float("inf")
        
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]
        while bfs:
            x, y = bfs.popleft()

            for dx, dy in directions:
                i, j = x + dx, y + dy
            
                if 0 <= i < m and 0 <= j < n and mat[i][j] > mat[x][y] + 1:
                    bfs.append((i,j))
                    mat[i][j] = mat[x][y] + 1
        return mat


