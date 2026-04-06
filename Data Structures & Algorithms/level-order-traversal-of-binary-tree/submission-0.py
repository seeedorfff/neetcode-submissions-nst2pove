# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base case
        if not root: return []
        
        # level order
        queue = deque([root])
        levels = [] # main output

        # bfs
        while queue: 
            n = len(queue) # snapshot to maintain levels
            curLevel = [] # keeps everything in the current level

            for _ in range(n):
                # pop from the queue and add children
                popped = queue.popleft()

                if popped.left: queue.append(popped.left)
                if popped.right: queue.append(popped.right)

                curLevel.append(popped.val)
            
            levels.append(curLevel)
        
        return levels

