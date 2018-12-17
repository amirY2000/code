class Node:
    
    def __init__(self,data):
        """
        making three node(left,data,right)
        """
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        """
        return the tree
        >>>__str__(5)
        (None)<-5->(None)
        """
        return "("+str(self.left)+")"+"<-"+ str(self.data) + "->" +"("+str(self.right)+")"

class BST:
    
    def __init__(self,tree_list:list):
        """
        get a list and put the first element as the root 
        of the tree and change the root to Node
        """
        self.tree_list = tree_list
        if len(tree_list) == 0:
            self.root = None
        else:
            self.root = Node(tree_list[0]) 
            for i in range(1,len(tree_list)):
                self.append(tree_list[i])  
    
    def append(self,value:list):
        """
        append a new value to the tree
        >>>a = BST([])
        >>>a.append(5)
        >>>print(a)
        (None)<-5->(None)
        """
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
                    while current.left is not None:
                        if value > current.data:
                            if current.right is not None:
                                current = current.right
                            else:
                                break                    
                        else:    
                            current = current.left
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
                    while current.right is not None:
                        if value < current.data:
                            if current.left is not None:
                                current = current.left
                            else:
                                break
                        else:    
                            current = current.right
                    current.right = Node(value)
    def search(self,value:list)->bool:
        """
        searching through the tree and return True iff
        the value is in the tree
        >>>a = BST([5,3,4,2,7,6,8])
        >>>a.search(5)
        True
        """
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
                current = self.root.left
                while current.data != value:
                    if value > current.data:
                        current = current.right 
                    else:    
                        current = current.left
                return True
            return False
    
    def remove(self, value:int):
        """
        remove a node from the tree
        >>>a = BST([5,3,2,4,7,6,8])
        >>>a.remove(5)
        (((None)<-2->(None))<-3->((None)<-4->(None)))<-6->(((None))<-7->((None)<-8->(None)))
        """
        if value >= self.root.data:
            self.swap(value , self.getmin(self.root.right))
            parent = self.root
            current = parent.right
            while current.data != self.getmin(self.root.right):
                parent = current
                current = parent.left
            parent.left = current.right
        else:
            if value < self.root.data:
                self.swap(value , self.getmax(self.root.left))
                parent = self.root
                current = parent.left
                while current.data != self.getmax(self.root.left):
                    parent = current
                    current = parent.right
                parent.right = current.left
    
    def swap(self,value,value1):
        if value == self.root.data:
            node = self.root
        else:
            if value > self.root.data:
                current = self.root.right
                while current.data != value:
                    if value < current.data:
                        current = current.left
                    else:
                        current = current.right
                node = current
            if value < self.root.data:
                current = self.root.left
                while current.data != value:
                    if value > current.data:
                        current = current.right 
                    else:    
                        current = current.left
                node = current
        if value1 == self.root.data:
            node1 = self.root
        else:
            if value1 > self.root.data:
                current = self.root.right
                while current.data != value1:
                    if value1 < current.data:
                        current = current.left
                    else:
                        current = current.right
                node1 = current
            if value1 < self.root.data:
                current = self.root.left
                while current.data != value1:
                    if value1 > current.data:
                        current = current.right 
                    else:    
                        current = current.left
                node1 = current        
        node.data , node1.data = node1.data , node.data

    def getmin(self,node):
        """
        return the smallest node
        >>>a = BST([5,3,4,2,7,6,8])
        >>>a.getmin(root)
        2
        >>>a = BST([5,3,4,2,7,6,8])
        >>>a.getmin(root.right)
        6
        """
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def getmax(self,node):
        """
        return the greatest node 
        >>>a = BST([5,3,4,2,7,6,8])
        >>>a.getmax(root)
        8
        >>>a = BST([5,3,4,2,7,6,8])
        >>>a.getmin(root.left)
        4
        """
        current = node
        while current.right is not None:
            current = current.right
        return current.data
    
    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)
    def _inorder(self,node):
        """
        print the tree inorder traversal
        >>>a = BST([5,3,4,2,7,6,8])
        >>>print(a)
        2
        3
        4
        5
        6
        7
        8
        """
        if node is not None:
            self._inorder(node.left)
            print(str(node.data))
            self._inorder(node.right)
    
    def preorder(self):
        if self.root is not None:
            self._preorder(self.root)
    def _preorder(self,node):
        """
        print the tree in preorder traversal
        >>>a = BST([5,3,4,2,7,6,8])
        >>>print(a)
        5
        3
        2
        4
        7
        6
        8
        """
        if node is not None:
            print(str(node.data))
            self._preorder(node.left)
            self._preorder(node.right)
    
    def postorder(self):
        if self.root is not None:
            self._postorder(self.root)
    def _postorder(self,node):
        """
        print the tree in postorder traversal
        >>>a = BST([5,3,4,2,7,6,8])
        >>>print(a)
        2
        4
        3
        6
        8
        7
        5
        """
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(str(node.data))
    
    def rooot(self):
        return self.root.data
    
    def __str__(self):
        #return str(self.inorder())
        #return str(self.preorder())
        return str(self.postorder())
        #return str(self.root)
