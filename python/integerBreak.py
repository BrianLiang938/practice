class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        three = n // 3
        if n - 3 * three == 1:
            three -= 1
            return pow(3, three) * 4
        elif n - 3 * three == 2:
            return pow(3, three) * 2
        else:
            return pow(3, three)