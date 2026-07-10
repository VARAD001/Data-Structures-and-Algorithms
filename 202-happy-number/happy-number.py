class Solution:
    def isHappy(self, n: int) -> bool:
        origin = set()
        while n != 1 and n not in origin:
            origin.add(n)
            total = 0
            while n>0:
                n,last_digit = divmod(n,10)
                total += last_digit**2
            n = total
        return n == 1
        