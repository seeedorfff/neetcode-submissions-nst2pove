class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cntS, cntT = {}, {} # char : cnt

        for i in range(len(s)):
            cntS[s[i]] = cntS.get(s[i], 0) + 1
            cntT[t[i]] = cntT.get(t[i], 0) + 1
        
        return cntS == cntT