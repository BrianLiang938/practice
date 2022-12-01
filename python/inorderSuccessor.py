# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        out = p
        if p.right != None:
            out = p.right
            while out.left != None:
                out = out.left
            return out
        else:
            parent = None
            if p.val < root.val:
                parent = root
                out = root.left
            else:
                out = root.right
            while out != None and out.val != p.val:
                if p.val < out.val:
                    parent = out
                    out = out.left
                else:
                    out = out.right
            return parent
                