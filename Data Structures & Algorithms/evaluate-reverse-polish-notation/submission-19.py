class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        if n == 1:
            return int(tokens[0])
        stack = []
        for i in range(n):    
            if tokens[i] != "+" and tokens[i] != "*" and tokens[i] != "-" and tokens[i] != "/":
                stack.append(int(tokens[i]))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                output = 0
                if tokens[i] == "+":
                    output = op2 + op1
                elif tokens[i] == "-":
                    output = op2 - op1                                
                elif tokens[i] == "*":
                    output = op2 * op1
                elif tokens[i] == "/":
                    output = math.trunc(op2 / op1)
                stack.append(output)
        return stack[0]