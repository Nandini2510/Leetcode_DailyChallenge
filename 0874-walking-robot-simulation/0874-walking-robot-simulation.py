class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0, -1), (-1, 0)] # N, E, S, W
        x,y = 0, 0
        idx = 0
        max_dist = 0
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -1:
                idx = (idx + 1) % 4
            elif command == -2:
                idx = (idx - 1) % 4
            else:
                dx, dy = directions[idx]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_dist = max(max_dist, x * x + y * y)
                    else:
                        break
        return max_dist
