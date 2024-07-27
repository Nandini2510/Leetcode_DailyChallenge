class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            stack.append(ch)

            while len(stack) >= 3 and stack[-1] == 'c' and stack[-2] == 'b' and stack[-3] == 'a':
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack) == 0
        