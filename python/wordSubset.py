class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mFreq = [0] * 26
        out = []
        for word in words2:
            temp = [0] * 26
            for c in word:
                temp[ord(c) - ord('a')] += 1
            for n in range(len(temp)):
                if temp[n] > mFreq[n]:
                    mFreq[n] = temp[n]
        print(mFreq)
        for word in words1:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            if all(x >= y for x, y in zip(freq, mFreq)):
                out.append(word)
        return out