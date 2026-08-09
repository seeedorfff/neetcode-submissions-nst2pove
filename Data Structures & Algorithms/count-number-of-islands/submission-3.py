class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def spread(r, c):
            # find all adjacent 1s
            # makes them 0
            # iterate till no more
            dxns = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            for dr, dc in dxns:
                nr, nc = r + dr, c + dc

                """ 
                conditions for spread 
                1. in bounds 
                2. grid content 1 
                """
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    grid[nr][nc] == "0"):
                    continue
                grid[nr][nc] = "0"
                spread(nr, nc)
        
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    spread(r, c)
                    res += 1
        return res
        
