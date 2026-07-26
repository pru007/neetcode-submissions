from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        pacific = [(row,0) for row in range(rows)] + [(0,col) for col in range(cols)]
        atlantic = [(row,cols-1) for row in range(rows)] +[(rows-1,col) for col in range(cols)]
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and heights[nr][nc]>=heights[r][c] and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return visited
        res = bfs(pacific) & bfs(atlantic)
        result = [[r,c] for r,c in res]
        return result
            