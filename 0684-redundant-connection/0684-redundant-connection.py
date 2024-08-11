class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
    
    def findUParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self, u, v):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)
        # this means u and v belong to same subset and doing union on them would form a cycle
        if ulp_u == ulp_v:
            return False
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ds = DisjointSet(n)
        res = []
        for u,v in edges:
            if not ds.unionByRank(u, v):
                res.append(u)
                res.append(v)
                break
        return res
