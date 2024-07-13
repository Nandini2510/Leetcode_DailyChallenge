class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""
        for st in strs:
            s += st
            s += "\n"
        return s

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        arr = []
        st = ""
        for ch in s:
            if ch != '\n':
                st += ch
            else:
                arr.append(st)
                st = ""
        return arr

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))