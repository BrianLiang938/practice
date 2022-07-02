class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        hCut = [horizontalCuts[0]]
        vCut = [verticalCuts[0]]
        for i in range(1, len(horizontalCuts)):
            hCut.append(horizontalCuts[i] - horizontalCuts[i-1])
        hCut.append(h - horizontalCuts[-1])
        for i in range(1, len(verticalCuts)):
            vCut.append(verticalCuts[i] - verticalCuts[i-1])
        vCut.append(w - verticalCuts[-1])
        return max(hCut) * max(vCut) % 1000000007