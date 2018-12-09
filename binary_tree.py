class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return "("+str(self.left)+")"+"<-"+ str(self.data) + "->" +"("+str(self.right)+")"

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
                    if value < current.data:
                        if current.left is not None:
                            current = current.left
                        else:
                            break
                    else:    
                        current = current.right
                if value < current.data:
                    current.left = Node(value)    
                if value > current.data:
                    current.right = Node(value)
            if value < self.root.data:
                current = self.root
                while current.left is not None:
                    if value > current.data:
                        if current.right is not None:
                            current = current.right
                        else:
                            break                    
                    else:    
                        current = current.left
                if value < current.data:
                    current.left = Node(value)    
                if value > current.data:
                    current.right = Node(value)

    def search(self,value):
        if value == self.root.data:
            return True
        else:
            if value > self.root.data:
                current = self.root.right
                while current.data != value:
                    if value < current.data:
                        current = current.left
                    else:
                        current = current.right
                return True
            if value < self.root.data:
                current = self.root
                while current.data != value:
                    if value > current.data:
                        current = current.right 
                    else:    
                        current = current.left
                return True
            return False
    
    def remove(self, value):
        pass
        if self.search(value) is True:
            if value == self.root.data:
                node1 = self.root
                node2 = Node(self.getmin(self.root.right)) 
                node1.data = None
                node1.data = node2.data
                node2.data = None
                self.root = node1              

    
    def getmin(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)
    def _inorder(self,node):
        if node is not None:
            self._inorder(node.left)
            print(str(node.data))
            self._inorder(node.right)
    
    def preorder(self):
        if self.root is not None:
            self._preorder(self.root)
    def _preorder(self,node):
        if node is not None:
            print(str(node.data))
            self._preorder(node.left)
            self._preorder(node.right)
    
    def postorder(self):
        if self.root is not None:
            self._postorder(self.root)
    def _postorder(self,node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(str(node.data))
    
    def __str__(self):
        return str(self.inorder())
        #return str(self.preorder())
        #return str(self.postorder())
        #return str(self.root)
