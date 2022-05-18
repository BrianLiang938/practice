class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        input = list(s)
        length = 0
        temp = 0
        map = {}
        for i in range(len(input)):
            if input[i] in map:
                if map[input[i]] < i - temp:
                    map[input[i]] = i
                    temp += 1
                    if temp > length:
                        length = temp
                else:
                    temp = i - map[input[i]]
                    map[input[i]] = i
            else:
                map[input[i]] = i
                temp += 1
                if temp > length:
                    length = temp
        return length