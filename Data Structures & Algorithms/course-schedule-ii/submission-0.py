class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1

        q = deque(c for c in range(numCourses) if indegree[c]==0)
        taken=0
        result = []
        while q:
            crs = q.popleft()
            result.append(crs)
            taken+=1
            for nxt in adj[crs]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    q.append(nxt)
        if taken==numCourses:
            return result
        else:
            return []