class Solution:
    def hammingWeight(self, n: int) -> int:
        length = 0
        count = 0
        while (n):
            count += (n & 1)
            length += 1
            n >>= 1
        return count