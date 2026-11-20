# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #with HELP
        return self.allowed(root, float('inf'), float('-inf'))
    def allowed(self, node: TreeNode, hi, lo):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return self.allowed(node.left, node.val, lo) and self.allowed(node.right, hi, node.val)

        