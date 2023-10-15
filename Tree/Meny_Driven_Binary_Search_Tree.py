class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def insert(node,data):
    if node is None:
        return Node(data)
    else:
        if data<node.data:
            node.left=insert(node.left,data)
        else:
            node.right=insert(node.right,data)
        return node

def printInorder(node):
    if node is not None:
        printInorder(node.left)
        print(node.data,"->",end=" ")
        printInorder(node.right)
        
def printPreorder(node):
    if node is not None:
        print(node.data,"->",end=" ")
        printPreorder(node.left)
        printPreorder(node.right)

def printPostorder(node):
    if node is not None:
        printPostorder(node.left)
        printPostorder(node.right)
        print(node.data,"->",end=" ")
    
def search(node,data):
    while node!=None:
        if data==node.data:
            return "FOUND"
        else:
            if data<node.data:
                node=node.left
            else:
                node=node.right
    return "NOT FOUND"
    
def minimum(node):
    if node==None:
        return "Empty tree"
    else:
        while node.left!=None:
            node=node.left
        return node.data
        
def height(node):
    if node is None:
        return 0
    else:
        return 1+ max(height(node.left),height(node.right))
    
    
class BinarySearchTree:
    def __init__(self,data):
        self.root=Node(data)
    
    def insertNode(self,data):
        self.root=insert(self.root,data)
            
    def inOrder(self):
        if self.root==None:
            print("Empty tree")
        else:
            printInorder(self.root)
            print(None)
            print()
    
    def preOrder(self):
        if self.root==None:
            print("Empty tree")
        else:
            printPreorder(self.root)
            print(None)
            print()
            
    def postOrder(self):
        if self.root==None:
            print("Empty tree")
        else:
            printPostorder(self.root)
            print(None)
            print()
        
    def searchNode(self,data):
        print(search(self.root,data))
        
    def minValue(self):
        return minimum(self.root)
        
    def heightOfBst(self):
        return height(self.root)


flag=True       
while True:
    print('----------------------')
    print('\n1. Insert in tree\n2. Get inorder Traversal\n3. Get preorder Traversal\n4. Get postorder Traversal\n5. Search element x\n6. Get minimum value\n7. Get height of tree\n0. Exit')
    print('----------------------')
    ch = int(input('\nEnter your choice : '))
    
    if ch == 1:
        if flag:
            bst=BinarySearchTree(int(input("Enter the value of root :")))
            flag=False
        else:
            bst.insertNode(int(input("Enter value to be inserted :")))

    elif ch == 2:
        bst.inOrder()
        
    elif ch == 3:
        bst.preOrder()
    
    elif ch == 4:
        bst.postOrder

    elif ch == 5:
        bst.searchNode(int(input("Enter the value of x :")))
        
    elif ch == 6:
        print("Minimum value in BST IS: " , bst.minValue())
        
    elif ch == 7:
        print("Height of BST is :", bst.heightOfBst())
       
    elif ch == 0:
        print("You have exited the program")
        break
    
    else:
        print("Wrong Input")
        