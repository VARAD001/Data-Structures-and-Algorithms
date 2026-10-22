class Solution:
    def validPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        while L < R:
            if s[R] != s[L]:
                skipL = s[L + 1:R + 1]
                skipR = s[L:R]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            L += 1
            R -= 1
        return True