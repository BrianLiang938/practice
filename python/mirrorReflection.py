class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        points = p / q
        newP = p
        while points % 1 != 0:
            newP += p
            points = newP / q
        if points % 2 == 0:
            return 2
        elif points % 2 == 1:
            if (newP / p) % 2 == 0:
                return 0
            else:
                return 1
        return -1