class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.lookUp(s, wordDict)
    def lookUp(self, s, wordDict):
        flag = 0
        print("s", s)
        if len(s) == 0:
            print("ehre")
            return 1
        else:
            for n in range(len(wordDict)):
                if wordDict[n][0] == s[0] and len(wordDict[n]) < len(s):
                    if len(wordDict[n] == )
                    flag = self.lookUp(s[len(wordDict[n]):], wordDict)
                    if flag == 1:
                        return 1
            return 0
            
