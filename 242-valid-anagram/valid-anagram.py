class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        for char in s:
            if char not in seen.keys():
                seen[char] = 1
            else:
                seen[char] += 1
        for char in t:
            if char in seen.keys():
                seen[char] -= 1
                if seen[char] == 0:
                    seen.pop(char,None)
            else:
                return False
        if not seen:
            return True
        return False

        