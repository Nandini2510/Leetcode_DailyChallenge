class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        vis = set()
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        def dfs(edge, prev):
            if edge in vis:
                return False
            vis.add(edge)
            for nei in adjList[edge]:
                if nei == prev:
                    continue
                if not dfs(nei, edge):
                    return False
        
            return True
        
        return dfs(0, -1) and len(vis) == n