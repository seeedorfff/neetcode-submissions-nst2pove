class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, preq in prerequisites:
            graph[course].append(preq)
        
        res = []
        visiting, completed = set(), set()

        def complete(course):
            if course in completed:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)

            for preq in graph[course]:
                if not complete(preq):
                    return False
            
            visiting.remove(course)
            completed.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not complete(i):
                return []
        return res