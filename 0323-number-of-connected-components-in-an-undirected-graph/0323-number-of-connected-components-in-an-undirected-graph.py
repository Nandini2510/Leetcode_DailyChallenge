class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = set()
        res = 0
        stack = []
        adjList = defaultdict(list)

        for edge in edges:
            from_node = edge[0]
            to_node = edge[1]
            adjList[from_node].append(to_node)
            adjList[to_node].append(from_node)
        
        for i in range(n):
            if i not in vis:
                res += 1
                stack.append(i)
                while stack:
                    curr = stack[-1]
                    stack.pop()
                    if curr not in vis:
                        vis.add(curr)
                    for neighbor in adjList[curr]:
                        if neighbor not in vis:
                            stack.append(neighbor)
        return res

            