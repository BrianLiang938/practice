# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
        order = []
        def inorder(root):
            if root == None:
                return
            if root.left != None:
                inorder(root.left)
            order.append(root.val)
            if root.right != None:
                inorder(root.right)
        inorder(root)
        return order[k - 1]
