class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node, prev_node):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in graph[node]:
                if nei == prev_node:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)