class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        strlen = len(s)
        if strlen % 2 != 0:
            return False
        for i in range(strlen):
            if s[i] == "(" or s[i] == "{" or s[i] == "[" :
                stack.append(s[i])                
            else:
                if len(stack) == 0:
                    return False
                bracket = stack.pop(len(stack)-1)
                if (s[i] == ")" and bracket != "(") or (s[i] == "}" and bracket != "{") or (s[i] == "]" and bracket != "["):
                    return False
        if stack != []:
            return False
        return True

