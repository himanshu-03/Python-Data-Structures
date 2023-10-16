# Program Name: binary_search_tree.py
# Implementing a binary search tree

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

class BinarySearchTree:
    def __init(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)

# Usage
bst = BinarySearchTree()
root = None
root = bst.insert(root, 50)
root = bst.insert(root, 30)
root = bst.insert(root, 20)
root = bst.insert(root, 40)
root = bst.insert(root, 70)
root = bst.insert(root, 60)
root = bst.insert(root, 80)
bst.inorder_traversal(root)
