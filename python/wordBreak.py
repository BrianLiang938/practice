class Solution:
    def word_break(s, words):
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in words:
                # runs and checks for substring inorder and then checks if prev substring is possible
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]