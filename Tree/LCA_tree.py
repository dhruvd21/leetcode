# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root == p:
                return p
            if root == q:
                return q
            if root == None:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)
            if lh != 0 and rh != 0:
                return root
            if lh == 0 and rh != 0:
                return rh
            if rh == 0 and lh != 0:
                return lh
            return 0

        return dfs(root)