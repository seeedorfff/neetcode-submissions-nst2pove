class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] # int

        for char in operations:
            if char == "D":
                stack.append(2 * stack[-1])
            elif char == "C":
                stack.pop()
            elif char == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(char))
        return sum(stack)