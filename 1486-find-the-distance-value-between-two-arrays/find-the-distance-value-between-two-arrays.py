class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0
        for x in arr1:
            L = 0
            R = len(arr2) 
            while L < R:
                mid = (L + R)//2   
                if arr2[mid] < x - d:
                    L = mid + 1     
                else:
                    R = mid
            count += L == len(arr2) or arr2[L] > x + d
        return count