class Solution:
    def isHappy(self, n: int) -> bool:
        origin = {}
        while n != 1:
            if n not in origin.keys():
                origin[n] = True
            else:
                return False
            n = str(n)
            suming = 0
            for i in n:
                suming += int(i)**2
            n = suming
        return True
        