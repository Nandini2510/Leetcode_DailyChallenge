class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        res = 0

        for i in range(len(tickets)):
            queue.append(i)

        while queue:
            index = queue.popleft()
            tickets[index] -= 1
            res += 1

            if tickets[index] == 0 and index == k:
                return res
            if tickets[index] > 0:
                queue.append(index)
        return res