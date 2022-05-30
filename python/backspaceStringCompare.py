class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        so = []
        to = []
        si = list(s)
        ti = list(t)
        for n in si:
            if n == '#' and len(so) > 0:
                so.pop()
            elif n != '#':
                so.append(n)
        for n in ti:
            if n == '#' and len(to) > 0:
                to.pop()
            elif n != '#':
                to.append(n)
        return so == to