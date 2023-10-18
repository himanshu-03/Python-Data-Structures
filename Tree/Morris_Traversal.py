#   Morris Traversal
#   Time Complexity = O(n)
#   Space Complexity = O(1) (Main advantage of using this traversal. Uses only constant space)
#                              1
#                             / \
#                            /   \
#                           2     3
#                          /  \
#                         /    \
#                        4      5
#                                \
#                                 \
#                                  6
#              
#                 Output --> 4 2 5 6 1 3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Morris-inorder traversal
def Morris_Traversal(root):
    morris = []
    cur = root

    while cur:
        if cur.left is None:
            morris.append(cur.val)
            cur = cur.right
        else:
            temp = cur.left
            while temp.right and temp.right != cur:
                temp = temp.right

            if temp.right is None:
                temp.right = cur
                cur = cur.left
            else:
                temp.right = None
                morris.append(cur.val)
                cur = cur.right

    return morris

if __name__ == '__main__':
    print("\033c", end='', flush=True)
    # Input tree elements
    root_val = int(input("Enter the value for the root: "))
    root = TreeNode(root_val)

    print('\n')
    queue = [root]
    while queue:
        current = queue.pop(0)
        left_val = int(input(f"Enter the value for the left child of {current.val} (Enter -1 for no child): "))
        if left_val != -1:
            current.left = TreeNode(left_val)
            queue.append(current.left)
        right_val = int(input(f"Enter the value for the right child of {current.val} (Enter -1 for no child): "))
        if right_val != -1:
            current.right = TreeNode(right_val)
            queue.append(current.right)
        print('\n')

    # Morris Traversal starts
    morris = Morris_Traversal(root)
    print(' '.join([str(i) for i in morris]))

