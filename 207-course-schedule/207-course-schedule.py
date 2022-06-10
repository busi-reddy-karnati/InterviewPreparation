#Let's do it with Khan's Algorithm
# Find nodes with 0 rank
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numFinished = 0
        rank = {}
        adj = {}
        for i in range(numCourses):
            rank[i] = 0
            adj[i] = []
        for prereq in prerequisites:
            rank[prereq[0]] += 1
            adj[prereq[1]].append(prereq[0])
        topSort = []
        for i in range(numCourses):
            if rank[i] == 0:
                topSort.append(i)
        while topSort:
            node = topSort.pop()
            numFinished += 1
            for neighbour in adj[node]:
                rank[neighbour] -= 1
                if rank[neighbour] == 0:
                    topSort.append(neighbour)
        return numFinished == numCourses
            
            