class Node():
    def __init__(self,data):
        """Initialize a Node with the input data and a next as None"""
        self.data = data
        self.next = None
    
    def __str__(self):
        '''link the value of Node to its next by a vector'''
        return str(self.data) + "->" + str(self.next)    

    def get_node(self):
        """
        return the value of the Node
        """
        return self.data
    
    def set_node(self,value:int):
        """set the value as node data"""
        self.data = value
        return self.data

class Linkedlist():
    def __init__(self,linked_list:list):
        '''get a list as linked_list and make a head from 
           the first element,then change its type to Node'''
        if len(linked_list) == 0:
            self.head = Node(None)   
        else:
            self.head = Node(linked_list.__getitem__(0))
            for i in range(1,len(linked_list)):
                self.append(linked_list.__getitem__(i))

    def __getitem__(self,position:int)->int:
        current = self.head
        i = 0
        while i != position:
            i += 1
            current = current.next
        return current.data       
    
    def __setitem__(self,position,value:int):
        length = self.__len__()
        if position > length:
            self.append(value)
        else:
            current = self.head
            i = 0 
            while i != position:
                i += 1
                current = current.next
            current.data = value    
    
    def append(self,last_node:int):
        """
        it's begin from the head of our linkedlist and find the last element and add new node
        >>>ll = Linkedlist([1,2,3])
        >>>ll.append(4)
        1->2->3->4->None
        """
        if self.head.get_node() == None:  
            self.head = Node(last_node)
        else: 
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(last_node)
    
    def __str__(self):
        ''' return the head as string '''
        return str(self.head) 
    
    def __len__(self):
        '''
        return the length of linked list
        >>>ll = Linkedlist([1,2,3])
        >>>ll.__len__()
        >>>3
        '''
        if self.head.get_node() == None:
            length = 0
        else:
            current = self.head
            length = 1
            while current.next != None:
                length += 1
                current = current.next
        return length    

    def __delitem__(self,position:int):

        """
        delete the the element of the linked list
        >>>ll = Linkedlist([1,2,3,4,5])
        >>>ll.__delitem__(4)
        1->2->3->5->None
        """
        current = self.head
        previous = None
        i = 0
        while i != position:
            i += 1
            previous = current
            current = current.next 
        if current.data == self.head.data:     
            self.head = current.next
        else:
            previous.next = current.next

    def reverse(self):
        '''reverse the linked list
        >>>ll = Linkedlist([1,2,3,4])
        >>>ll.reverse()
        3->2->1->None
        '''
        previous = None
        current = self.head 
        while current.next != None: 
            temp = current.next
            current.next = previous 
            previous = current 
            current = temp
        self.head = previous

    def pop(self):
        """
        delete the last node of our linkedlist
        >>>ll = Linkedlist([1,2,3])
        >>>ll.pop()
        1->2->None
        """
        length = self.__len__()
        current = self.head
        previous = None
        if length == 0:
            return 'there is nothing to remove'
        if length == 1:
            self.head = Node(None)
        else:
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = current.next

    def copy(self):
        """
        return a copy of Linkedlist
        >>>ll = Linkedlist([1,2,3])
        >>>ll.copy()
        1->2->3->None
        """
        copy = Linkedlist([])
        current = self.head
        copy.append(current.data)
        while current.next is not None:
            copy.append(current.next.data)
            current = current.next
        return copy

    def extend(self,new_list:list):
        """
        add new list to the linkned list
        >>>l = [1,2,3], new_list = [4,5,6]
        >>>l.extend(new_list)
        1->2->3->4->5->6->None
        """
        for i in range(0,len(new_list)):
            copy_head = Node(new_list.__getitem__(i))
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = copy_head    

    def swap(self,position1,position2):
        '''
        change two elemnts of the list with each other
        >>>ll = 1->2->3->None
        >>>swap(ll,1,2)
        >>>2->1->3->None
        '''
        length = self.__len__()
        if position1 > length or position2 > length:
            return "im not responsible for positions out of range "
        previous1 = None 
        index1 = self.head
        previous2 = None
        index2 = self.head
        counter = 1
        while counter < position1:
            previous1 = index1
            index1 = index1.next
            counter += 1
        counter = 1
        while counter < position2:
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
        """
        sort the linked_list by bubble_sort
        >>>ll = 2->1->3->None
        >>>bubble_sort(ll)
        >>>1->2->3->None
        """
        length = self.__len__()
        if length == 0 :
            return 'There is nothing to'
        for i in range(0,length):
            current = self.head
            for _j in range(0,length-i-1):
                if current.data > current.next.data:
                    self.swap(_j+1,_j+2)#+1 and +2 are return to swaping because in swaping the positions are from 1 to another positive position, +1 and +2 are for fitting the positions for swap
                else:
                    current = current.next

    def selectionsort(self):
        length = self.__len__()
        for i in range(length): 
            min_idx = i
            for j in range(i+1, length):
                if self.head[min_idx] > self.head[j]: 
                    min_idx = j          
            temp = self.head[min_idx]
            self.head[min_idx] = self.head[i]
            self.head[i] = temp
        
