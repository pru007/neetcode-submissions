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
        track = []
        results = []
        track.append([root])
        while track:
            curr = track[0]
            temp1 = []
            for elem in curr:
                temp1.append(elem.val)
            results.append(temp1)
            temp = []
            for elem in curr:
                if elem.left:
                    temp.append(elem.left)
                if elem.right:
                    temp.append(elem.right)
            if temp:
                track.append(temp)
            del track[0]

        return results
        
