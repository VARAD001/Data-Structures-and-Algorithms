# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node:
                return 0
            left_length = get_height(node.left)
            if left_length == -1:
                return -1
            right_length = get_height(node.right)
            if right_length == -1:
                return -1
            if abs(left_length - right_length) > 1:
                return -1
            return 1 + max(left_length,right_length)
        return get_height(root) != -1

        
        