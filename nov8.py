def largest(mylist:list)->int:
    '''
    find the largest elemnt of the list
    >>>l = [1,2,3,4,5]
    >>>largest(l)
    5
    '''
    i = 0
    for j in mylist:
        if j > i:
            i = j
    return i        
print(largest([1,4,2,5]))                
               
def remove_duplicates(mylist:list)->list:
    '''
    return a copy of list that has no duplicate elements
    >>>l = [1,2,3,2]
    >>>remove_duplicates(l)
    [1,2,3]
    '''
    list_copy = []
    for i in mylist:
        if i not in list_copy:
            list_copy.append(i)        
    return list_copy
print(remove_duplicates([2, 2, 4, 5, 6, 4, 'a', 'a', 'a', '3'])) 

def commen_element(mylist,yourlist:list)->list:
    '''
    return True if list1 and list2 have at least one element in commen
    >>>l1 = [1,2,4,3] , l2 = [1,7,6,8]
    >>>commen_element(l1,l2)
    True
    '''
    for i in mylist:
        for j in yourlist:
            if i == j:
                return True
    return False
print(commen_element([1,2,3,4],[5,7,8]))            

def list_to_string(mylist:list)->list:
    '''
    change the type oof each element to string
    >>>l = [1,2,'a']
    >>>list_to _string(l)
    ['1','2','a']
    '''
    new_list = []
    for i in mylist:
        if type(i) != str:
            i = str(i)
        new_list.append(i)
    return new_list
print(list_to_string([1,2,'a']))

def extend_a_list(mylist,yourlist:list)->list:
    '''
    add list2 to the end of list1
    >>>l1 = [1,2] , l2 = [3,4]
    >>>extend_a_list(l1,l2)
    [1,2,3,4]
    '''
    for i in yourlist:
        mylist.append(i)
print(extend_a_list([1,2],[3,4]))

def all_squares(max_number:int)->list:
    '''
    return a list of all the squares from 0 to max_numbers
    >>>all_squares(15)
    [1,2,3]
    '''
    new_list = []
    for i in range(max_number + 1):
        if i * i <= max_number:
            new_list.append(i*i)
    return new_list
print(all_squares(26))

def items_in_common(mylist,yourlist:list)->list:
    '''
    return a list that lis1 and list2 have in common
    >>>l1 = [1,2] , l2 = [2,3]
    >>>items_in_common(l1,l2)
    [2]
    '''
    for j in yourlist:
        if j not in mylist:
            yourlist.remove(j)
    return yourlist
print(items_in_common([1,2],[2,3]))

def mystery_12(list_of_numbers,upper_limit:list)->bool:
    """
    it will show that our input as upper_limit is the biggest number in our list of not
    >>>l = [1,2,3]
    >>>mystery_12(l,3)
    True
    """
    b = True
    for e in list_of_numbers:
        if e > upper_limit:
            b = False
    return b        
print(mystery_12([1,2,3,4,5],5))
