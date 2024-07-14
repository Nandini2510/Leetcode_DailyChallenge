class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxHeight = 0

        while i < j:
            h = min(height[i], height[j])
            width = j - i
            maxHeight = max(maxHeight, h * width)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return maxHeight