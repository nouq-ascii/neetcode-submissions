class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        strlen = len(s)
        brackets = {"(": ")", "{": "}", "[": "]"}
        if strlen % 2 != 0:
            return False
        for i in range(strlen):
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

