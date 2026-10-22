class Solution:
    def validPalindrome(self, s: str) -> bool:
        self.count = 1
        return self.ispalindrome(s,0,len(s)-1)
        
    def ispalindrome(self,strs,L,R):        
        while L < R:
            if strs[L] != strs[R]:
                if self.count == 1:
                    self.count -= 1
                    return self.ispalindrome(strs,L+1,R) or self.ispalindrome(strs,L,R-1)
                else:
                    return False
            L += 1
            R -= 1
        return True
        