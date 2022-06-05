# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        output = root
        if root == None:
            return root
        else:
            output = self.recur(root.val, root.left, root.right)
        return output
    def recur(self, val, left, right) -> Optional[TreeNode]:
        temp = TreeNode(val)
        if left != None and right != None:
            temp = TreeNode(val, self.recur(right.val, right.left, right.right), self.recur(left.val, left.left, left.right))
        elif left == None and right != None:
            temp = TreeNode(val, self.recur(right.val, right.left, right.right), None)
        elif left != None and right == None:
            temp = TreeNode(val, None, self.recur(left.val, left.left, left.right))
        return temp