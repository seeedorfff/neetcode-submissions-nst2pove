class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, preq in prerequisites:
            graph[course].append(preq)

        res = []
        visit, cycle = set(), set()

        def can_complete(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for preq in graph[course]:
                if not can_complete(preq):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not can_complete(course):
                return []
        return res