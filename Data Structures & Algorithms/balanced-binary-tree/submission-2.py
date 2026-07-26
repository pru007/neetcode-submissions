# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        result = True
        def dfs(root):
            nonlocal result
            if not root:
                return 0
            left_d = dfs(root.left)
            right_d = dfs(root.right)
            if abs(left_d-right_d) >1:
                result = False
            return 1+max(left_d,right_d)
        dfs(root)
        return result
            