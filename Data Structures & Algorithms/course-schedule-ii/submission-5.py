class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for crs, preq in prerequisites:
            graph[crs].append(preq)
        
        res = []
        visiting, completed = set(), set()

        def can_complete(crs):
            if crs in completed:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for preq in graph[crs]:
                if not can_complete(preq):
                    return False
            visiting.remove(crs)
            completed.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not can_complete(i):
                return []
        return res