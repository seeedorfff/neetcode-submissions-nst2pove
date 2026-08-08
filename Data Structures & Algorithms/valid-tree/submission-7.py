class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visited = set()

        def dfs(node, p_node):
            if node in visited:
                return False
            
            visited.add(node)

            for nei_node in graph[node]:
                if nei_node == p_node:
                    continue
                if not dfs(nei_node, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n