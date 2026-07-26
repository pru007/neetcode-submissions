from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        rarea = float("-inf")
        def bfs(sr,sc):
            area = 1
            q = deque()
            q.append((sr,sc))
            visited.add((sr,sc))
            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        area+=1
                        q.append((nr,nc))
                        visited.add((nr,nc))
            return area
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    rarea = max(rarea,bfs(row,col))
        return 0 if rarea==float("-inf") else rarea