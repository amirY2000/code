class Node():
    def __init__(self,data):#make a node with input value "data"
        self.data = data
        self.next = None
    def __str__(self):# change the type of node from id to str
        return str(self.data) + "->" + str(self.next)    
class Linkedlist():
    def __init__(self,linked_list):# get a list name "linked_list" and linkes each element to each other(Linked list) 
        if len(linked_list) == 0:# when linked_list be empty it will set the value of head as None
            self.head = Node(None)   
        else:# when linked isn't empty the first element of our input list will be set as head
            self.head = Node(linked_list[0])
            for i in range(1,len(linked_list)):
                self.add_node(linked_list[i])
    def add_node(self,last_node):# find the last node(a node that doesn't have next term) from the head and then add new node(last_node) to the linked_list
        if self.head.data == None:# when the linked_list is empty and we want to add new node, it will change the value of head to new node  
            self.head = Node(last_node)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(last_node)
    def __str__(self):# return the head a str
        return str(self.head) 
    def __len__(self):# retturn the length of our linked list
        if self.head.data == None:
            length = 0
        else:
            current = self.head
            length = 1
            while current.next != None:
                length += 1
                current = current.next
        return length

mylist = Linkedlist([])
print(len(mylist))
print(mylist)