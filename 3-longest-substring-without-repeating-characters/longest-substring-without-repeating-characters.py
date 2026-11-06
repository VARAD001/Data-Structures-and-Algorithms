class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        L = 0
        seen = [0]*128
        for R in range(len(s)):
            char = ord(s[R])
            while seen[char] > 0 :
                seen[ord(s[L])] -= 1
                L += 1
            seen[char] += 1
            res = max(res,R - L + 1)
        return res
        