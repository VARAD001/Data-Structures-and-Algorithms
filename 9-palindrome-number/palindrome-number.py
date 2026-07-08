class Solution:
    def __pal(self,num,left,right):
        if left > right:
            return True
        if num[left] != num[right]:
            return False
        return self.__pal(num,left + 1, right-1)
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        return self.__pal(num,0,len(num)-1)