class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join(char.lower() for char in s if char.isalnum())
        l, r = 0, len(newS) - 1

        while l < r:
            if newS[l] != newS[r]:
                return False
            
            l += 1
            r -= 1
        return True