class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        

        for i in range(1, len(strs)):
            word = strs[i]
            temp = ""
            for j in range(min(len(word), len(res))):
                if(word[j] != res[j]):
                    break
                temp += word[j]
            res = temp
        return res



    
        




