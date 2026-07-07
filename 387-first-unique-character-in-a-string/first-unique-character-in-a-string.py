class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter = {}
        for char in s :
            letter[char] = letter[char] + 1 if char in letter else 1
        for temp in range(len(s)):
            if letter[s[temp]] == 1:
                return temp
        return -1

        