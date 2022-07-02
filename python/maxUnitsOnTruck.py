class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda boxTypes: boxTypes[1], reverse = True)
        out = 0
        for sub in boxTypes:
            if truckSize > sub[0]:
                truckSize -= sub[0]
                out += sub[0] * sub[1]
            else:
                out += sub[1] * truckSize
                return out
        return out