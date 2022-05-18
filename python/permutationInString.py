class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return 0
        string1 = list(s1)
        string2 = list(s2)
        index1 = [0] * 26
        index2 = [0] * 26
        for n in range(len(string1)):
            index1[ord(string1[n]) - ord('a')] += 1
            index2[ord(string2[n]) - ord('a')] += 1
        if index2 == index1:
            return 1
        for n in range(len(string2) - len(string1)):
            index2[ord(string2[n]) - ord('a')] -= 1
            index2[ord(string2[n + len(string1)]) - ord('a')] += 1
            if index2 == index1:
                return 1
        return 0