class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = 0
        res = temperatures

        while i < len(temperatures):
                
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            i += 1
        while stack:
            res[stack[-1]] = 0
            stack.pop()
        return res
            
