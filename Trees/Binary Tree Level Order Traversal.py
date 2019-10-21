"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
import queue
from Trees.helper import make_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        level_collection = list()
        q = queue.Queue()
        q.put([root])
        while not q.empty():
            roots = q.get()
            if roots:
                val_list = []
                root_list = []
                for root in roots:
                    if root:
                        val_list.append(root.val)
                        root_list.append(root.left)
                        root_list.append(root.right)
                q.put(root_list)
                if val_list:
                    level_collection.append(val_list)
        return level_collection

"""
Runtime: O(n)
"""
if __name__ == "__main__":
    node_list = []
    tree = make_tree(node_list, 0)
    lol = Solution()
    print(lol.levelOrder(tree))


