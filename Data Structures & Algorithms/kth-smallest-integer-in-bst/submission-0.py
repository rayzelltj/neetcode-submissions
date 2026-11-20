# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in order traversal
        values = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                values.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        
        values.sort()
        return values[k-1]

