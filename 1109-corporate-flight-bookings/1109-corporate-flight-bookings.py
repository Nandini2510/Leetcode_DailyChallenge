class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        mp = defaultdict(int)
        res = [0] * n

        for booking in bookings:
            first = booking[0]
            last = booking[1]
            seats = booking[2]
            for i in range(first, last + 1):
                mp[i] += seats
        
        for i in range(1, n + 1):
            res[i - 1] = mp[i]
        return res
        