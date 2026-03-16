# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        ans = []
        while queue:
            arrlen = len(queue)
            level = []
            for i in range(arrlen):
                root = queue.pop(0)
                if root:
                    level.append(root.val)
                    queue.append(root.left)
                    queue.append(root.right)
# appending the last (rightmost) element of every level to ans
            if level:
                ans.append(level[-1])
        return ans