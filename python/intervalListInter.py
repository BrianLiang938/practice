class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        i = j = 0
        output = []
        first = second = -1
        while i < n and j < m:
            bot = max([firstList[i][0], secondList[j][0]])
            top = min([firstList[i][1], secondList[j][1]])
            if bot <= top:
                output.append([bot, top])
            if firstList[i][1] > secondList[j][1]:
                j += 1
            elif firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                i += 1
        return output
        