class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def canFlow(r, c, acc): # if can flow, recurse
            if (r, c) in acc:
                return
            
            acc.add((r, c))

            dxns = [[0, -1], [0, 1], [-1, 0], [1, 0]]

            for dr, dc in dxns:
                nr, nc = r + dr, c + dc

                # conditions for can't flow
                # out of bounds both row + col
                # OUTSIDE to INSIDE, nei must be high
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    heights[nr][nc] < heights[r][c]):
                    continue
                
                canFlow(nr, nc, acc)
        
        
        pacific = set()
        for r in range(rows):
            canFlow(r, 0, pacific)
        for c in range(cols):
            canFlow(0, c, pacific)
        
        atlantic = set()
        for r in range(rows):
            canFlow(r, cols-1, atlantic)
        for c in range(cols):
            canFlow(rows-1, c, atlantic)

        return [list(cell) for cell in pacific.intersection(atlantic)]
