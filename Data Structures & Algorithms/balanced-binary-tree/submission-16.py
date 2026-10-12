class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(root):
            nonlocal balanced

            if not root or not balanced:
                return 0

            left = dfs(root.left)
            if not balanced:
                return 0

            right = dfs(root.right)
            if not balanced:
                return 0

            if abs(left - right) > 1:
                balanced = False
                return 0

            return 1 + max(left, right)

        dfs(root)
        return balanced