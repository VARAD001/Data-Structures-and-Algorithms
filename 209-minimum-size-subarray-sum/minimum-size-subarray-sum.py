class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        res = float('inf')
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        for i in range(n):
            L = i + 1
            R = n
            req = target + prefix[i]
            while L <= R:
                mid = (L + R)//2
                if prefix[mid] >= req:
                    R = mid - 1
                    res = min(res,mid - i)
                else:
                    L = mid + 1
        return 0 if res == float('inf') else res

        