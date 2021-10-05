# URL : https://leetcode.com/problems/path-sum/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(totalval,node):
            if node==None:
                return False
            elif node.left == None and node.right == None and node.val+totalval == targetSum:
                    return True
            else:
                return traverse(node.val+totalval,node.left) or traverse(node.val+totalval,node.right)
        return traverse(0,root)
                