class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0
        R = k - 1
        while R < len(arr) - 1 :
            if abs(x - arr[R + 1]) >= abs(x - arr[L]):
                if arr[L + 1:R+2] != arr[L:R + 1]:
                    return arr[L:R+1]
            R += 1
            L += 1
        return arr[L : R + 1]