class Node():
    def __init__(self,data):
        """Initialize a Node with the input data and a next as None"""
        self.data = data
        self.next = None
    
    def __str__(self):
        '''link the value of Node to its next by a vector'''
        return str(self.data) + "->" + str(self.next)    

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

    def __getitem__(self, position:int)->int:
        if position >= len(self):
            raise IndexError("Position is out of range")
        current = self.head
        i = 0
        while i < position:
            i += 1
            current = current.next
        return current.data       
    
    def __setitem__(self,position,value:int):
        length = len(self)
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
        it is adding a new node to the end of the linkedlist
        >>>ll = Linkedlist([1,2,3])
        >>>ll.append(4)
        1->2->3->4->None
        """
        if self.head.data == None:  
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
        if self.head.data == None:
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
        delete an index from the linked list
        >>>ll = Linkedlist([1,2,3,4,5])
        >>>ll.__delitem__(4)
        1->2->3->5->None
        """
        current = self.head
        previous = None
        i = 0
        while i != position and self.head != None:
            i += 1
            previous = current
            current = current.next 
        if current.data == self.head.data:     
            self.head = current.next
        else:
            previous.next = current.next

    def reverse(self):
        '''
        reverse the linked list
        >>>ll = Linkedlist([1,2,3,4])
        >>>ll.reverse()
        3->2->1->None
        '''
        length = len(self)
        for i in range(length//2):
            temp = self[length-i-1]
            self[length-i-1] = self[i]
            self[i] = temp
    
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
    
    def bubble_sort(self):
        """
        sort the linked_list by bubble_sort
        >>>ll = 2->1->3->None
        >>>bubble_sort(ll)
        >>>1->2->3->None
        """
        length = len(self)
        for i in range(length):
            for j in range(0,length-i-1):
                if self[j] > self[j+1]:
                    temp = self[j+1]
                    self[j+1] = self[j]
                    self[j] = temp

    def selection_sort(self):

        """
        sort the linked list by selection_sort
        """
        length = len(self)
        for i in range(length):
            min_index = i
            for j in range(i+1,length):
                if self[min_index] > self[j]:
                    min_index = j
            temp = self[min_index]
            self[min_index] = self[i]
            self[i] = temp        

    def insertion_sort(self):
        '''
        sort linkedlist by insertion_sort
        '''
        length = len(self)
        for i in range(1,length):
            temp = self[i] 
            j = i-1
            while j >=0 and temp < self[j]: 
                self[j+1] = self[j] 
                j -= 1
            self[j+1] = temp    
