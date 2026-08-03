class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1

        q = deque(c for c in range(numCourses) if indegree[c]==0)
        taken=0
        while q:
            crs = q.popleft()
            taken+=1
            for nxt in adj[crs]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    q.append(nxt)
        return taken==numCourses