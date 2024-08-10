class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        A course has 3 possible states:
        1. visited -> crs has been added to output
        2. visiting -> crs not added to output, but added to cycle
        3. unvisited -> crs not added to output or cycle
        
        """
        adjList = defaultdict(list)
        vis, cycle = set(), set()
        output = []
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in vis:
                return True
            cycle.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            vis.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
         
        return output
