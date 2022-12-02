class Solution:
    def sieve(self, c, marked):
        i = 2
        while c * i < len(marked) - 1:
            marked[c*i] = True
        i = c + 1
        for j in range(c + 1, len(marked) - 1):
            if j == False:
                self.sieve(j, marked)
                return
        return
    def countPrimes(self, n: int) -> int:
        marked = [False] * (n+1)
        self.sieve(2, marked)
        out = 0
        for i in range(1, len(marked)):
            if marked[i] == False:
                out += 1
        return out