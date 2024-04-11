class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(m, target):
            l, r = 0, len(m) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if m[mid] == target:
                    return True
                elif m[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        for i in range(len(matrix)):
            res = binarySearch(matrix[i], target)
            if res:
                return True
        return False