class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = collections.defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node, vis):
            if node == destination:
                return True
            vis.add(node)
            for neighbor in adjList[node]:
                if neighbor not in vis:
                    if dfs(neighbor, vis):
                        return True
            return False
        
        vis = set()
        return dfs(source, vis)

        