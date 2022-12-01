class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        totalA = (ay2 - ay1) * (ax2 - ax1)
        totalB = (by2 - by1) * (bx2 - bx1)
        xOverlap = min(ax2, bx2) - max(ax1, bx1)
        yOverlap = min(ay2, by2) - max(ay1, by1)
        if xOverlap > 0 and yOverlap > 0:
            return totalA + totalB - (xOverlap * yOverlap)
        return totalA + totalB