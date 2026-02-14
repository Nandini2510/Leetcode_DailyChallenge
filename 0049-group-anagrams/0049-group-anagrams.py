class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = defaultdict(list)

        for word in strs:
            sortedW = "".join(sorted(word))
            hashmap[sortedW].append(word)
        for k, v in hashmap.items():
            res.append(v)
        
        return res

        