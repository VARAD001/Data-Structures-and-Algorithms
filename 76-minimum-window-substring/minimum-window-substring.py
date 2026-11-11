class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char,0) + 1
        res = 10000000000,None,None
        L = 0
        formed = 0
        window_count = {}
        for R in range(len(s)):
            window_count[s[R]] = window_count.get(s[R],0) + 1
            char = s[R]
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            while L <= R and formed == len(t_count):
                rem = s[L]
                if R - L + 1 < res[0]:
                    res = (R - L + 1, L , R)
                window_count[rem] -= 1
                if rem in t_count and window_count[rem] < t_count[rem]:
                    formed -= 1
                L += 1

        if res[0] == 10000000000:
            return ""
        else:
            return s[res[1]:res[2] + 1]
