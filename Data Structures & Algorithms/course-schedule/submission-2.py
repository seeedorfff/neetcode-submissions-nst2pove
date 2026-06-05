class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, preq in prerequisites:
            graph[course].append(preq)
        
        visiting = set()

        def dfs(node):
            if graph[node] == []: return True
            if node in visiting: return False

            visiting.add(node)
            for preq in graph[node]:
                if not dfs(preq): return False
            visiting.remove(node)
            graph[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True
            