class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for crs, preq in prerequisites:
            graph[crs].append(preq)

        visiting = set()
        completed = set()

        def can_complete(node):
            if node in completed:
                return True
            if node in visiting:
                return False

            visiting.add(node)

            for nei_node in graph[node]:
                if not can_complete(nei_node):
                    return False
            visiting.remove(node)
            completed.add(node)
            return True
        
        for i in range(numCourses):
            if not can_complete(i):
                return False
        return True