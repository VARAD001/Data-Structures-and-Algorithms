class Solution:
    def trap(self, height: list[int]) -> int:
        L = 0
        R = len(height) -1
        maxL = height[L]
        maxR = height[R]
        total = 0
        while L < R:
            if maxL < maxR:
                L += 1
                maxL = max(height[L],maxL)
                total += max(0,maxL - height[L])
            else:
                R -= 1
                maxR = max(height[R],maxR)
                total += max(0,maxR - height[R])
        return total
            