class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0:1}
        current = 0
        res = 0
        for i in range(len(nums)):
            current += nums[i]
            if current - k in prefix_map:
                res += prefix_map[current-k]
            prefix_map[current] = prefix_map.get(current,0) + 1
        return res
        
        