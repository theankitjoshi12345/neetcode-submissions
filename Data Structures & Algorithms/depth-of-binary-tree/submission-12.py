# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        left = 1 + self.maxDepth(root.left) if root.left else 1
        right = 1 + self.maxDepth(root.right) if root.right else 1

        return max(left, right)
        