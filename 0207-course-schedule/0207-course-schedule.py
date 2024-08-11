class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        vis = set()
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(crs):
            if crs in vis:
                return False
            if adjList[crs] == []:
                return True
            vis.add(crs)
            for nei in adjList[crs]:
                if not dfs(nei):
                    return False
            vis.remove(crs)
            adjList[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True