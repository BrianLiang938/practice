class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == None or s == "":
            return True
        if t == None or t == "":
            return False
        sp = tp = 0
        while tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
                if sp == len(s):
                    return True
            else:
                tp += 1
        return False