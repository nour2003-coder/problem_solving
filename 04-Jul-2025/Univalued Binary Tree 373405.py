# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue=deque()
        queue.append(root)
        while(queue):
            val=root.val
            a=queue.popleft()
            if a.val == val:
                if a.right:
                    queue.append(a.right)
                if a.left:
                    queue.append(a.left)
            else:
                return False
        return True

