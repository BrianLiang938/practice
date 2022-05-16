class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]] += chars[s[i]]
            else:
                chars[s[i]] = 1
        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i
        return -1


