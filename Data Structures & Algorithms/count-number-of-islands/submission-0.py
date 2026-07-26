from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        count = 0

        def bfs(sr,sc):
            q = deque()
            q.append((sr,sc))
            visited.add((sr,sc))
            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1' and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    count+=1
                    bfs(r,c)
        return count
