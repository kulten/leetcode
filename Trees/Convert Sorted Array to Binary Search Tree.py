"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if len(nums) == 0:
            return
        mid = len(nums)//2
        tree = TreeNode(nums[mid])
        tree.left = self.sortedArrayToBST(nums[:mid])
        tree.right = self.sortedArrayToBST(nums[mid+1:])
        return tree

"""
Runtime: O(n)
"""

if __name__ == "__main__":
    lol = Solution()
    node_list = [-10,-3,0,5,9]
    print(lol.sortedArrayToBST(node_list))
