# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # no child -> delete
        # 1 child -> delete and plug in child
        # 2 children -> right -> left -> left...

        if not root:
            return root

        # search for node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # found node
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            # successor
            # right, left, left,...
            curr = root.right
            while curr.left:
                curr = curr.left
            # copy the successor value into the node(to be deleted)
            root.val = curr.val

            # check within the right subtree and delete the node we copied
            root.right = self.deleteNode(root.right, root.val)
        return root

