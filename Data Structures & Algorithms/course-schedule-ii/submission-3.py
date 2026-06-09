class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        visiting, completed = set(), set()
        res = []

        def dfs(course):
            if course in visiting:
                return False
            if course in completed:
                return True
            
            visiting.add(course)
            for preq in graph[course]:
                if not dfs(preq):
                    return False
            
            visiting.remove(course)
            completed.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res