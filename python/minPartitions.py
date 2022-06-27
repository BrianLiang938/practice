class Solution:
    def minPartitions(self, n: str) -> int:
        out = 0
        m = int(n)
        while m > 0:
            temp = m % 10
            m = m // 10
            if temp > out:
                out = temp
        return out