class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp1 = [0] * len(text1)
        for n in range(len(text2)):
            if text2[n] in text1 and n < :
