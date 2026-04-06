class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                substr = "" # keep the letters
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() # removes the open brac

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

            else:
                stack.append(char)
        return "".join(stack)