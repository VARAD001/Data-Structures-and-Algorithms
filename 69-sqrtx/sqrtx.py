class Solution:
    def mySqrt(self, x: int) -> int:
        if 2 > x:
            return x
        L = 1
        R = x//2
        while L <= R:
            mid = (L + R)//2
            if mid > x//mid:
                R = mid - 1
            elif mid < x//mid:
                L = mid + 1
            else:
                return mid
        return R

         