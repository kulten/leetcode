class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_tree(node_list, index=0):
    if index >= len(node_list) or node_list[index] is None:
        return None
    node = node_list[index]
    left = 2*index + 1
    right = 2* index + 2
    tree = TreeNode(node)
    tree.left = make_tree(node_list, left)
    tree.right = make_tree(node_list, right)
    return tree