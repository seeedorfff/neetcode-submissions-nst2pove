# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            n = len(q)
            n_level = []

            for _ in range(n):
                node = q.popleft()

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

                n_level.append(node.val)
            if n_level:
                res.append(n_level)
        return res
        