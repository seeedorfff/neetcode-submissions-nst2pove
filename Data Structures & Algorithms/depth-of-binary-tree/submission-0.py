# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # using the bfs approach
        if not root:
            return 0
        
        queue = deque([root]) # FIFO
        level = 0

        while queue:
            n = len(queue)

            for _ in range(n):
                popped = queue.popleft()

                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            
            level += 1
        return level