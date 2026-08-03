class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join(char.lower() for char in s if char.isalnum())

        return (newS == newS[::-1])