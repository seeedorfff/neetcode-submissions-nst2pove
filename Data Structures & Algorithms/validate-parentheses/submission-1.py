class Solution:
    def isValid(self, s: str) -> bool:
        paranMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = [] # only open paran

        for c in s:
            if c in paranMap:
                if stack and stack[-1] == paranMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack