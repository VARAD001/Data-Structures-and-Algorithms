class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = [0]*256
        map_t = [0]*256
        for i in range(len(s)):
            char_s = ord(s[i])
            char_t = ord(t[i])
            if map_s[char_s] != map_t[char_t]:
                return False
            map_s[char_s] = i + 1
            map_t[char_t] = i + 1
        return True