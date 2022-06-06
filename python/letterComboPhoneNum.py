class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        if len(digits) == 0:
            return output
        self.create(digits, "", output)
        return output
    def create(self, digits, current, output):
        if(len(digits) == 0):
            output.append(current)
            return
        currDigit = digits[0]
        added = ""
        if currDigit == "2":
            added = "abc"
        elif currDigit == "3":
            added = "def"
        elif currDigit == "4":
            added = "ghi"
        elif currDigit == "5":
            added = "jkl"
        elif currDigit == "6":
            added = "mno"
        elif currDigit == "7":
            added = "pqrs"
        elif currDigit == "8":
            added = "tuv"
        elif currDigit == "9":
            added = "wxyz"
        for i in range(len(added)):
            self.create(digits[1:], current + added[i], output)
        
