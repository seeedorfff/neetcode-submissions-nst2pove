class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        visiting = set()
        def dfs(node, prev_node):
            if node in visiting:
                return False
            
            visiting.add(node)
            for nei_node in graph[node]:
                if nei_node == prev_node:
                    continue
                if not dfs(nei_node, node):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True
            
        
        return dfs(0, -1) and n == len(visited)