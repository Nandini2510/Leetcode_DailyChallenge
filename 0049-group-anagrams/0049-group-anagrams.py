class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        ans = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in mp:
                mp[sorted_word].append(word)
            else:
                mp[sorted_word].append(word)
        
        for val in mp.values():
            ans.append(val)
        return ans



'''
1. Create a map of list, Iterate each w through list
2. sort the w, check if sort w matches any key in map
3. if it matches, we append the original w to that list of key value
4. It it doesn't matches we will create a new pair (key, value)
'''