# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left and not root.right:
            length = 1 + self.minDepth(root.left)
        elif not root.left and root.right:
            length = 1 + self.minDepth(root.right)
        else:
            left_length = self.minDepth(root.left)
            right_length = self.minDepth(root.right)
            length = 1 + min(left_length,right_length)
        return length

        