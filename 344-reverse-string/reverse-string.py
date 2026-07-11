class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(str,left,right):
            if left > right:
                return
            s[left],s[right] = s[right],s[left]
            return reverse(s,left + 1,right-1)
        reverse(s,0,len(s)-1)
        