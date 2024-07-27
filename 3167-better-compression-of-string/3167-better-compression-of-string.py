class Solution:
    def betterCompression(self, compressed: str) -> str:
        mp = defaultdict(int)
        s = ""
        i = 0

        while i < len(compressed):
            letter = compressed[i]
            count = ""
            i += 1
            while i < len(compressed) and compressed[i].isdigit():
                count += compressed[i]
                i += 1
            mp[letter] += int(count)   
        sort_map = {key: mp[key] for key in sorted(mp)}
        for key, val in sort_map.items():
            s += key
            s += str(val)
        return s
        

        