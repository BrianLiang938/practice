# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        pivot = int(n / 2)
        while left != right:
            if isBadVersion(pivot + 1):
                if pivot == 0:
                    return 1
                if not(isBadVersion(pivot1)):
                    return pivot
                else:
                    right = pivot
                    pivot = int(left + ((right - left) / 2))
            else:
                left = pivot
                pivot = int(left + ((right - left) / 2))