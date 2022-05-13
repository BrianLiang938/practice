class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for n in range(len(words) - 1):
            first = words[n]
            second = words[n+1]
            if(len(first) <= len(second)):
                tie = 1
                length = len(first)
            else:
                tie = 0
                length = len(second)
            for i in range(length):
                if order.find(first[i]) < order.find(second[i]):
                    break
                elif order.find(first[i]) > order.find(second[i]):
                    return 0
                if i == length - 1 and not(tie):
                    return 0
        return 1
