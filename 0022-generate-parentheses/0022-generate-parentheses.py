class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(open, close, n, s):
            if open == n and close == n:
                ans.append(s)
                return
            if open > close and open != n:
                dfs(open + 1, close, n, s + "(")
                dfs(open , close + 1, n, s + ")")
            if open == n:
                dfs(open, close + 1, n, s + ")")
            if open == close:
                dfs(open + 1, close, n, s + "(")
            
        dfs(0,0,n,"")
        return ans

