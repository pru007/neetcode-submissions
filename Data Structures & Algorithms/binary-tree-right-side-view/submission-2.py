# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        allLevels = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                elem = q.popleft()
                level.append(elem.val)
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
            if level:
                allLevels.append(level[-1])
        return allLevels