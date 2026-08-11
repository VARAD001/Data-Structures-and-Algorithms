class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        a = 0
        max_avg = 0
        for i in range(k):
            count += arr[i]
        if count/k >= threshold:
            a +=1 
        for i in range(k,len(arr)):
            count += arr[i]
            count -= arr[i-k]
            if count/k >= threshold:
                a += 1
        return a

        