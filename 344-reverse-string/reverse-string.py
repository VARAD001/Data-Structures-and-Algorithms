class Solution:
    def reverseString(self, s: list[str]) -> None:
        stack = []
        for i in range(len(s)-1,-1,-1):
            stack.append(s[i])
        s[:] = stack
        