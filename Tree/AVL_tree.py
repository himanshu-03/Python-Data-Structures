class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance(root)

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance(root)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def balance(self, node):
        if not node:
            return node
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

# Example usage:
if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None
    keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for key in keys:
        root = avl_tree.insert(root, key)

    print("Inorder Traversal of AVL tree:")
    avl_tree.inorder_traversal(root)

    key_to_delete = 10
    root = avl_tree.delete(root, key_to_delete)
    print("\nAfter deleting", key_to_delete)
    avl_tree.inorder_traversal(root)

class AVLTreeMenu:
    def __init__(self):
        self.avl_tree = AVLTree()
        self.root = None

    def display_menu(self):
        print("AVL Tree Menu:")
        print("1. Insert a key")
        print("2. Delete a key")
        print("3. Display the AVL tree")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                key = int(input("Enter the key to insert: "))
                self.root = self.avl_tree.insert(self.root, key)
                print(f"Key {key} inserted.")
            elif choice == "2":
                key = int(input("Enter the key to delete: "))
                self.root = self.avl_tree.delete(self.root, key)
                print(f"Key {key} deleted.")
            elif choice == "3":
                print("Inorder Traversal of AVL tree:")
                self.avl_tree.inorder_traversal(self.root)
            elif choice == "4":
                print("Exiting the AVL Tree Menu.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    avl_tree_menu = AVLTreeMenu()
    avl_tree_menu.run()
