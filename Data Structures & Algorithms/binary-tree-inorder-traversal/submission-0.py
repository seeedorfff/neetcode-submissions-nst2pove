# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left -> node -> right
        res = []
        def inorder(node):
            if not node:
                return 
            
            node.left = inorder(node.left)
            res.append(node.val)
            node.right = inorder(node.right)
        
        inorder(root)
        return res