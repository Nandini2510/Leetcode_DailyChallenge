class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        mp = defaultdict(list)

        for val in strs:
            temp = ''.join(sorted(val))
            mp[temp].append(val)
        
        for val in mp.values():
            ans.append(val)
        return ans
        