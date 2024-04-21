class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(land), len(land[0])

        def dfs(i, j, r1, c1, r2, c2):
            if (i<0 or i>=m) or (j < 0 or j >= n):
                return
            if land[i][j] == 1:
                land[i][j] = 2
                r1[0] = min(r1[0], i) 
                c1[0] = min(c1[0], j) 
                r2[0] = max(r2[0], i)
                c2[0] = max(c2[0], j)
                dfs(i+1, j, r1, c1, r2, c2)
                dfs(i, j+1, r1, c1, r2, c2)
                dfs(i-1, j, r1, c1, r2, c2)
                dfs(i, j-1, r1, c1, r2, c2)
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    r1 = [i]
                    c1 = [j]
                    r2 = [i]
                    c2 = [j]
                    dfs(i, j, r1, c1, r2, c2)
                    res.append([r1[0], c1[0], r2[0], c2[0]])
        return res
