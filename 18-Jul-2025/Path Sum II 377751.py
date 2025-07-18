# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(root,path,target):
            if not(root):
                return
            target+=root.val
            path.append(root.val)
            if not(root.left) and not(root.right) and target ==  targetSum:
                res.append(path[:])
                
            dfs(root.left,path,target)
            dfs(root.right,path,target)
            path.pop()
        dfs(root,[],0)
        return(res)