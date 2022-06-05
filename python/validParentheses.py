class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif len(stack) == 0:
                return 0
            elif char == ']':
                check = stack.pop()
                if check != '[':
                    return 0
            elif char == '}':
                check = stack.pop()
                if check != '{':
                    return 0
            elif char == ')':
                check = stack.pop()
                if check != '(':
                    return 0
        if len(stack) == 0:
            return 1
        else:
            return 0