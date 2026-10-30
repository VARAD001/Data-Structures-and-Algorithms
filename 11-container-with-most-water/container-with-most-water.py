class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        L = 0
        R = len(height) - 1
        while L < R:
            area = (R - L) * min(height[L],height[R])
            res = max(res,area)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return res