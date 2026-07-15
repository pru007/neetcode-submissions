# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = deque()
        stack.append(root)
        result = []
        while len(stack)>0:
            temp = []
            for i in range(len(stack)):
                elem = stack.popleft()
                temp.append(elem.val)
                if elem.left:
                    stack.append(elem.left)
                if elem.right:
                    stack.append(elem.right)
                # stack.popleft()
            result.append(temp)
        return result