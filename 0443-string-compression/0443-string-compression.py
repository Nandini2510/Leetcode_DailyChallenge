class Solution:
    def compress(self, chars: List[str]) -> int:
        s = uniqChar = ""
        count = 0
        ans = 0
        for i in range(len(chars)):
            if uniqChar == "":
                uniqChar = chars[i]
                count += 1
            elif uniqChar == chars[i]:
                count += 1
            else:
                chars[ans] = uniqChar
                ans += 1
                if count > 1:
                    for c in str(count):
                        chars[ans] = c
                        ans += 1
                count = 1
                uniqChar = chars[i]
        chars[ans] = uniqChar
        ans += 1
        if count > 1:
            for c in str(count):
                chars[ans] = c
                ans += 1

        return ans
