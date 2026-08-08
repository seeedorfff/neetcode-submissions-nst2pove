class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles
        # all nodes connected

        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visiting = set()
        visited = set()

        def dfs(node, p_node):
            if node in visiting: return False

            visiting.add(node)

            for nei_node in graph[node]:
                if nei_node == p_node: 
                    continue
                if not dfs(nei_node, node):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True
        
        return dfs(0, -1) and len(visited) == n