# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __isSym(self,left,right):
        if not left and not right :
            return True
        if left and right:
            if left.val == right.val:
                cond_a = self.__isSym(left.left,right.right)
                cond_b = self.__isSym(right.left,left.right)
                return cond_a and cond_b
        return False
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.__isSym(root.left,root.right)
        