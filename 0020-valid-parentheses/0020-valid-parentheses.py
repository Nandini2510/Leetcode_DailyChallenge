class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if stack:
                    if (stack[-1] == '{' and ch == '}') or (stack[-1] == '[' and ch == ']') or (stack[-1] == '(' and ch == ')'):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
        return True if not stack else False



'''
1. Create a stack (list)
2. If open bracket -> push into stack
3. If close bracket -> pop from top of stack and check corresponding closing bracket
4. if stack is empty 
'''
        
        