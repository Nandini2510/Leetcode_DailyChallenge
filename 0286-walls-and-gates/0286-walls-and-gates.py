class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        vis = [[0] * cols for _ in range(rows)]
        q = deque()
        delR = [-1, 0, 1, 0]
        delC = [0,1,0,-1]
        
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0 and not vis[i][j]:
                    q.append((0, (i, j)))
                    vis[i][j] = 1
       
        while q:
            dist, (r,c) = q.popleft()
            for i in range(4):
                nr = r + delR[i]
                nc = c + delC[i]
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or vis[nr][nc] == 1 or rooms[nr][nc] == -1 or rooms[nr][nc] == 0:
                    continue
                vis[nr][nc] = 1
                rooms[nr][nc] = dist + 1
                q.append((dist + 1, (nr, nc)))

        
        