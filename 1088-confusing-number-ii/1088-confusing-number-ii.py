matching = {'1':'1', '6':'9', '9':'6', '8':'8', '0':'0'}
def is_confusing(n_str) -> bool:
    if len(n_str) == 1:
        return n_str not in {'0', '1', '8'}
    left = 0
    right = len(n_str) - 1

    while left <= right:
        if matching[n_str[left]] != n_str[right]:
            return True
        left += 1
        right -= 1
    return False

class Solution:
    def backtrack(self, val_str, val):
        if 1 <=val<=self.n:
            if is_confusing(val_str):
                self.total += 1
        elif val > self.n:
            return
        
        for c in matching.keys():
            if val == 0:
                if c == '0':
                    continue
                self.backtrack(val_str + c, val * 10 + int(c))
            else:
                self.backtrack(val_str + c, val * 10 + int(c))

    def confusingNumberII(self, n: int) -> int:
        self.n = n
        self.total = 0
        self.backtrack('', 0)

        return self.total
        