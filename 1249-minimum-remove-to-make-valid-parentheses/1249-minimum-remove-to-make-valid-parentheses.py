class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        s = list(s)
        
        for i, char in enumerate(s):
            if char == "(":
                st.append(i)
            elif char == ")":
                if st:
                    st.pop()
                else:
                    s[i] = ''
        
        while st:
            s[st.pop()] = ''
        
        return ''.join(s)
        