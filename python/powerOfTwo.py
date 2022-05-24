class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        length = 0
        count = 0
        while (n):
            count += (n & 1)
            length += 1
            n >>= 1
        if count == 1:
            return 1
        else:
            return 0