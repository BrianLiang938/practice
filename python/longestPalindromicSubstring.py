class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = curr = s[0]
        left = right = 0
        flag = 1
        n = len(s)
        if n == 2:
            if s[-1] == s[0]:
                return s
            else:
                return s[0]
        for i in range(n):
            flag = 1
            left = right = i
            curr = s[i]
            while left > 0 and right < n - 1:
                if s[left - 1] == s[right + 1]:
                    curr = s[left - 1: right + 2]
                    left -= 1
                    right += 1
                    if s[left] == curr[1]:
                        flag = 0
                elif s[left - 1] == curr[-1] and flag == 1:
                    curr = s[left - 1:right + 1]
                    left -= 1
                elif s[right + 1] == curr[0] and flag == 1:
                    curr = s[left: right + 2]
                    right += 1
                else:
                    break
            if len(curr) > len(output):
                output = curr
            if left != 0 and s[left - 1] == curr[-1] and flag == 1:
                    curr = s[left - 1:right + 1]
                    left -= 1
            if right != len(s) - 1 and s[right + 1] == curr[0] and flag == 1:
                curr = s[left: right + 2]
                right += 1
        return output

def main():
    s = Solution()
    s.longestPalindrome("aaa")

if __name__ == "__main__":
    main()