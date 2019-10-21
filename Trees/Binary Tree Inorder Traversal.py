# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        traversal = []
        stack = list()
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            tmproot = stack.pop()
            traversal.append(tmproot.val)
            root = tmproot.right
        return traversal


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    lol = Solution()
    print(lol.inorderTraversal(tree))

