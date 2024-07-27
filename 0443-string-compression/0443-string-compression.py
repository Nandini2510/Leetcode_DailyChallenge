class Solution:
    def compress(self, chars: List[str]) -> int:
        uniqChar = ""
        count = 0
        ans = 0
        def write_chars(uniqChar, count):
            nonlocal ans
            chars[ans] = uniqChar
            ans += 1
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1
        for i in range(len(chars)):
            if uniqChar == "":
                uniqChar = chars[i]
                count += 1
            elif uniqChar == chars[i]:
                count += 1
            else:
                write_chars(uniqChar, count)
                count = 1
                uniqChar = chars[i]
        write_chars(uniqChar, count)
        return ans
