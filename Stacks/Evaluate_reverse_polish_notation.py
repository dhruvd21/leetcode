class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        for i in range(n):
            # All the different operations
            if tokens[i] == "+":
                ans = int(stack.pop()) + int(stack.pop())
                stack.append(ans)
            elif tokens[i] == "-":
                ans = -int(stack.pop()) + int(stack.pop())
                stack.append(ans)
            # Special case for division as questions wants us to round off the number near to zero, so when we compute a positive answer, we round off to the lowest nearest int, but it will be opposite for negative numbers as we are rounding off close to 0
            elif tokens[i] == "/":
                cur = int(stack.pop())
                div = stack.pop()
                ans = int(div) // cur
                if div%cur != 0 and ans < 0:
                    ans+=1
                stack.append(ans)
            elif tokens[i] == "*":
                cur = int(stack.pop())
                ans = int(stack.pop()) * cur
                stack.append(ans)
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]