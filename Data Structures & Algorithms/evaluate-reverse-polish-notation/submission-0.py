class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #only ints
        
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for tk in tokens:
            if tk in ops:
                b, a = stack.pop(), stack.pop()

                ans = ops[tk](a, b)

                stack.append(ans)
            else:
                stack.append(int(tk))
        return stack[-1]