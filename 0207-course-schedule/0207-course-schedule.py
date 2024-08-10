class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        vis = set()

        def dfs(crs):
            # detected loop
            if crs in vis:
                return False
            if adjList[crs] == []:
                return True
            vis.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            vis.remove(crs)
            adjList[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True