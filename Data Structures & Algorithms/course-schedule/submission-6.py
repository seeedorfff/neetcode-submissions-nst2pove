class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list) #crs -> preq
        for crs, preq in prerequisites:
            graph[crs].append(preq)

        visiting = set()

        def complete(crs):
            if graph[crs] == []:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)

            for preq in graph[crs]:
                if not complete(preq):
                    return False
            
            visiting.remove(crs)
            graph[crs] = []
            return True
        
        for i in range(numCourses):
            if not complete(i):
                return False
        return True