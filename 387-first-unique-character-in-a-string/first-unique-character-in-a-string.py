class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter = {}
        for char in s :
            letter[char] = letter.get(char,0) + 1
        for temp in range(len(s)):
            if letter[s[temp]] == 1:
                return temp
        return -1

        