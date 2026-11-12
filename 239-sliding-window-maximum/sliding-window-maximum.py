class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = collections.deque()
        L = R = 0
        while R < len(nums):
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)
            if (R + 1) >= k:
                res.append(nums[q[0]])
                if q[0] == L:
                    q.popleft()
                L += 1
            R += 1
        return res