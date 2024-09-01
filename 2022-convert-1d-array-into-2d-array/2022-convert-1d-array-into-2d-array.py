class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        arr = [[0 for _ in range(n)] for _ in range(m)]

        ind = 0

        while ind < len(original):
            for i in range(m):
                for j in range(n):
                    arr[i][j] = original[ind]
                    ind += 1
        return arr