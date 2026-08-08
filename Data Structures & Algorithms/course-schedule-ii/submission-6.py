class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            graph[crs].append(preq)
        
        visiting = set()
        visited = set()
        res = []

        def canFinish(crs):
            if crs in visiting: return False
            if crs in visited: return True

            visiting.add(crs)

            for preq in graph[crs]:
                if not canFinish(preq):
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not canFinish(i):
                return []
        return res