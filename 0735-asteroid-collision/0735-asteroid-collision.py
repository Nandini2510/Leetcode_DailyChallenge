class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if stack and asteroid < 0 < stack[-1]:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack

        

        
