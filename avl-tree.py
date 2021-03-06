import igraph
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.height = 1


class AvlTree:

    root = None

    def insert(self, val):
        self.root = self.binsert(self.root, val)
    
    def binsert(self, root, val):
        if root == None:
            return Node(val)
        elif root.val < val:
            root.right = self.binsert(root.right, val)
        else:
            root.left = self.binsert(root.left, val)

        root.height = 1 + max(self.height(root.left), 
                           self.height(root.right))
        bf = self.balance_factor(root)

        # Left Left 
        if bf > 1 and val < root.left.val: 
            return self.rightRotate(root) 
  
        # Right Right 
        if bf < -1 and val > root.right.val: 
            return self.leftRotate(root) 
  
        # Left Right 
        if bf > 1 and val > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Right Left 
        if bf < -1 and val < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root

    def leftRotate(self, root):
        right_child = root.right
        grand_child = right_child.left

        right_child.left = root
        root.right = grand_child

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        right_child.height = 1 + max(self.height(right_child.left), self.height(right_child.right))

        return right_child

    
    def rightRotate(self, root):
        left_child = root.left
        grand_child = left_child.right

        left_child.right = root
        root.left = grand_child

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        left_child.height = 1 + max(self.height(left_child.left), self.height(left_child.right))

        return left_child

    def balance_factor(self, root): 
        if not root: 
            return 0
  
        return self.height(root.left) - self.height(root.right) 
  

    def height(self, root):
        if root == None:
            return 0
        return root.height
    
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print(root.val) 
        self.preOrder(root.left) 
        self.preOrder(root.right)


myTree = AvlTree() 
  
myTree.insert(1) 
myTree.insert(2) 
myTree.insert(4) 
myTree.insert(7) 
myTree.insert(3) 
myTree.insert(5) 
  

print("Preorder traversal") 
myTree.preOrder(myTree.root) 