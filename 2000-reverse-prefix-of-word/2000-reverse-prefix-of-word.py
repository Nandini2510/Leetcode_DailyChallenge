class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = 0

        for i in range(len(word)):
            if word[i] == ch:
                ind = i
                break
        if ind == 0:
            return word
        ans = ""
        index = ind + 1
        while ind >= 0:
            ans += word[ind]
            ind -= 1
        
        for i in range(index, len(word)):
            ans += word[i]
        return ans

        # j = 0
        # while j < ind:
        #     word[j], word[ind] = word[ind], word[j]
        #     j = j + 1
        #     ind = ind - 1
        # return word