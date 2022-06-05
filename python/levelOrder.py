# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        s = Solution()
        output = []
        temp = [[root]]
        if root:
            output = [[root.val]]
            s.recur(output, temp)
        return output
    def recur(self, output, input):
        s = Solution()
        temp = []
        vals = []
        for n in input[-1]:
            if n.left != None:
                vals.append(n.left.val)
                temp.append(n.left)
            if n.right != None:
                vals.append(n.right.val)
                temp.append(n.right)
        if len(temp) > 0:
            input.append(temp)
            output.append(vals)
            s.recur(output,input)
