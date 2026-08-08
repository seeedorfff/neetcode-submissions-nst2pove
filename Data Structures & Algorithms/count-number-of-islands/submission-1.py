class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def spread(row, col):
            # finds all neighbors that are 1 (connected neighbors)
            dxns = [[0, -1], [0, 1], [-1, 0], [1, 0]]

            for dr, dc in dxns:
                nr = row + dr
                nc = col + dc

                # conditions for spread
                # out of bounds or cell is 0
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or 
                    grid[nr][nc] == "0"):
                    continue
                
                grid[nr][nc] = "0"
                spread(nr, nc)
                # remember anytime you call spread, change the value to 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # call spread (before that change to 0)
                    grid[r][c] = "0"
                    spread(r, c)
                    # as you call spread you have found an island so count
                    res += 1
        return res