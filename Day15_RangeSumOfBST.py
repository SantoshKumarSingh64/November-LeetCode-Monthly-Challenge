'''
Question Description :-
Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with
a value in the range [low, high].

 
Example 1:    
                10
              /    \ 
             5      15
           /  \      \ 
          3    7      18
        Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
        Output: 32

Example 2:
                10
              /    \ 
             5      15
           /  \    / \ 
          3    7  13  18
         /    /
        1    6 
        Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
        Output: 23
 
Constraints:
        1. The number of nodes in the tree is in the range [1, 2 * 104].
        2. 1 <= Node.val <= 105
        3. 1 <= low <= high <= 105
        4. All Node.val are unique.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        self.sum = 0
        
        def helper(root):
            
            if root is None:
                return 
                
            if low <= root.val <= high:
                self.sum += root.val
                
                helper(root.left)
                helper(root.right)
                
            if root.val < low:
                helper(root.right)
            
            elif root.val > high:
                helper(root.left)
                
        helper(root)
        
        return self.sum
        
