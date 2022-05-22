class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        oneBefore = 2
        twoBefore = 1
        output = 0
        for i in range(2,n):
            output = oneBefore +  twoBefore
            twoBefore = oneBefore
            oneBefore = output
        return output