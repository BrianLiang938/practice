class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.split(" ")
        output = ""
        for i in range(len(strings)):
            t = list(strings[i])
            left = 0
            right = len(t) - 1
            while left < right:
                temp = t[left]
                t[left] = t[right]
                t[right] = temp
                left += 1
                right -= 1
            if i == len(strings) - 1:
                output += ''.join(t)
            else:
                output += ''.join(t) + ' '
        return output
