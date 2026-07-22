# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if not p or not q:
            return None
        stack = deque()
        stack.append(root)
        while len(stack)>0:
            if p.val <= stack[-1].val and q.val >= stack[-1].val:
                return stack[-1]
            if p.val >= stack[-1].val and q.val <= stack[-1].val:
                return stack[-1]
            if p.val < stack[-1].val and q.val < stack[-1].val:
                stack.append(stack[-1].left)
                stack.popleft()
            if p.val > stack[-1].val and q.val > stack[-1].val:
                stack.append(stack[-1].right)
                stack.popleft()