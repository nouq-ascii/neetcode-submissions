class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for i in range(len(s)):
            c = s[i]
            if c in brackets:
                stack.append(c)                
            else:
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if c != brackets[item]:
                    return False

        if stack != []:
            return False
        return True

