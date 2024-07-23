class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = defaultdict(list)
        n = len(isConnected)
        stack = []
        vis = set()
        res = 0

        for i in range( n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adjList[i].append(j)
        
        for i in range(n):
            if i not in vis:
                res += 1
                stack.append(i)
                while stack:
                    curr = stack.pop()
                    if curr not in vis:
                        vis.add(curr)
                    for neighbor in adjList[curr]:
                        if neighbor not in vis:
                            stack.append(neighbor)
        return res
        
       

