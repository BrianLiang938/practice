class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        info = [0] * 26
        for char in magazine:
            info[ord(char) - ord('a')] += 1
        for char in ransomNote:
            info[ord(char) - ord('a')] -= 1
            if info[ord(char) - ord('a')] < 0:
                return 0
        return 1


