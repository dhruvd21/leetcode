# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        ans = []
        count = 0
        while queue:
            arrlen = len(queue)
            level = []
            count+=1
            
            for i in range(arrlen):
                root = queue.pop(0)
                if root:
                    level.append(root.val)
                    queue.append(root.left)
                    queue.append(root.right)
            if level:
                if count%2 == 0:
                    ans.append(level[::-1])
                else:
                    ans.append(level)
        return ans