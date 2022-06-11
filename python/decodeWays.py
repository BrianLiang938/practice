class Solution:
    def numDecodings(self, s: str) -> int:
        ret = self.search(s)
        return ret

    def search(self, s):
        output = 0
        if s == "0":
            return 0     
        if len(s) <= 1:
            return 1
        if s[0] == "0":
            return 0
        if s[0] == "1":
            output += self.search(s[2:])
        if s[0] == "2" and s[1] in ("0", "1", "2", "3", "4", "5", "6"):
            output += self.search(s[2:])
        output += self.search(s[1:])
        return output