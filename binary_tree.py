class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.left) +" "+ str(self.data) + " " + str(self.right)
class BST:
    def __init__(self,tree_list):
        if len(tree_list) == 0:
            self.root = None
        else:
            self.root = Node(tree_list[0]) 
            for i in range(len(tree_list)):
                self.append(tree_list[i])  
    def append(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            if value > self.root.data:
                current = self.root
                while current.right is not None:
                    current = current.right
                    if value < current.data:
                        break
                if value < current.data:
                    current.left = Node(value)    
                if value > current.data:
                    current.right = Node(value)
            if value < self.root.data:
                current = self.root
                while current.left is not None:
                    current = current.left
                    if value > current.data:
                        break
                if value < current.data:
                    current.left = Node(value)    
                if value > current.data:
                    current.right = Node(value)

    def search(self,value):
        if value == self.root.data:
            return True
        else:
            if value > self.root.data:
                current = self.root
                while current.right.data != value: 
                    current = current.right
                    if value < current.data:
                        current = current.left
                return True
            if value < self.root.data:
                current = self.root
                while current.left.data != value: 
                    current = current.left
                    if value > current.data:
                        current = current.right
                return True
        return False
       
    def __str__(self):
        return str(self.root)
    def tree(self):
        return str(self.root)


