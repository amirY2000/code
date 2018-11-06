import copy

class Node():
    def __init__(self,data):
        """
        Initialize a Node with the input data and a next as None
        """
        self.data = data
        self.next = None
    def __str__(self):
        '''
        link the value of Node to its next by a vector
        '''
        return str(self.data) + "->" + str(self.next)    
class Linkedlist():
    def __init__(self,linked_list):
        '''get a list as linked_list and make a head from 
           the first element,then change its type to Node
        '''
        if len(linked_list) == 0:
            self.head = Node(None)   
        else:
            self.head = Node(linked_list[0])
            for i in range(1,len(linked_list)):
                self.add_node(linked_list[i])
    def add_node(self,last_node):
        '''
        it's begin from the head of our linked list and find the last element and add new node
        '''
        if self.head.data == None:  
            self.head = Node(last_node)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(last_node)
    def __str__(self):
        '''
        return the head as string
        '''
        return str(self.head) 
    def __len__(self):
        '''
        return the length of linked list
        '''
        if self.head.data == None:
            length = 0
        else:
            current = self.head
            length = 1
            while current.next != None:
                length += 1
                current = current.next
        return length
    def swap(self,position1,position2):
        '''TODO: Can I make this more efficient?'''
        '''
        swap to elemnts of the list find them from their position
        >>>ll = 1->2->3->4->None
        >>>swap(ll,2,3)
        >>>1->3->2->4->None
        '''
        length = self.__len__()
        if position1 > length or position2 > length:
            return "im not responsible for positions out of range "        
        counter = 0
        previous1 = None 
        index1 = self.head
        previous2 = None
        index2 = self.head
        while counter < position1-1:
            previous1 = index1
            index1 = index1.next
            counter += 1
        counter = 0
        while counter < position2-1:
            previous2 = index2
            index2 = index2.next
            counter += 1  
        if previous1 != None:
            previous1.next = index2
        else:
            self.head = index2
        previous2.next = index1
        temp = index1.next
        index1.next = index2.next
        index2.next = temp


    def bubble_sort(self):
        length = self.__len__()
        for i in range(0,length):
            current = self.head
            for _j in range(0,length-i-1):
                if current.data > current.next.data:
                    self.swap(_j+1,_j+2)
                else:
                    current = current.next
