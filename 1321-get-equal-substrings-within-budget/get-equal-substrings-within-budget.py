class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = 0
        L = 0
        ans = 0
        def abso(R):
            return abs(ord(s[R])-ord(t[R]))
        for R in range(len(s)):
            diff += abso(R) 
            while diff > maxCost:
                diff -= abso(L)
                L += 1
            ans=max(ans,R-L+1)
        return ans
        