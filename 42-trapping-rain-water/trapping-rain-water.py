class Solution:
    def trap(self, height: list[int]) -> int:
        max_left = []
        anchor = 0
        for i in height:
            max_left.append(anchor)
            anchor = max(anchor,i)
        max_right = [0] * len(height)
        anchor = 0
        for i in range(len(height)-1,-1,-1):
            max_right[i] = anchor
            anchor = max(anchor,height[i])
        total = 0
        for i in range(len(height)):
            total += max(0,min(max_left[i],max_right[i])-height[i])
        return total

