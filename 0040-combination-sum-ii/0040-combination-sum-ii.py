class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        cand.sort()
        res = []
        
        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(cand)):
                if cand[i] == prev:
                    continue
                cur.append(cand[i])
                backtrack(cur, i+1, target - cand[i])
                cur.pop()
                prev = cand[i]
        backtrack([], 0, target)
        return res