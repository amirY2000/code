def every_other_new(liist:list)->list:
    """
    return a new list consisting of every other elements of the old list
    >>>l = [1,2,3,4,5] 
    >>>every_other_new(l)
    [1,_,3,_5]
    """
    lisst = []
    for i in range(0,len(liist)):
        if i % 2 != 0:
            lisst.append("_") 
        else:
            lisst.append(liist[i])
    return lisst 
print(every_other_new([1,2,3,4,5,6]))    

def every_other_modify(liist:list)->list:
    """
    Modify a list so that every other element except first element.
    >>>l = [1,2,3,4,5]
    >>>every_other_modify(l)
    [2,4]
    """
    liist = liist[1::2]
print(every_other_modify([1,2,3,4,5,6]))

def sum_of_even(list_of_numbers:list)->int:
    """
    return the sum of even elemnts of list
    >>>l = [1,2,3,4]
    >>>sum_of_even(l)
    6
    """
    s = 0
    for i in list_of_numbers:
        if i % 2 == 0:
            s += i
    return s
print(sum_of_even([1,2,3,4,5,6]))        

def collect_strings(liist:list)->list:
    """
    return a new list that consisting of the strings of old list
    >>>l = [1,'a']
    >>>collect_strings(l)
    ['a']
    """
    lisst = []
    for i in liist:
        if type(i) == str :
            lisst.append(i)
    return lisst
print(collect_strings(["a",1]))

def count_int(liist:list)->int:
    """
    return numbers of integers of list
    >>>li = [2,'a']
    >>>count_int(li)
    1
    """
    x = 0
    for i in liist:
        if type(i) == int :
            x += 1
    return x
print(count_int(["a",1]))

def remove_strings_modify(liist:list)->list:
    '''Modify the list by removing strings from the list
    >>>li = ['a',1]
    >>>remove_strings_modify(['a',1])
    [1]
    '''
    for i in liist:
        if type(i) == str:
            liist.remove(i)
            for j in liist:
                if type(j) == str:
                    liist.remove(j)      
print(remove_strings_modify(['1',8,'v','s',5,4,'d', 'c']))

def mystery_10(list_of_number:list)->list:
    '''
    it makes a new list and will add the numbers that are bigger than a limit to new list.
    but this code will return an error because we didn't define the variable 'limit'.
    Here is an example if we define the limit as '2':
    >>>l = [1,2,3,4,5]
    >>>mystery_10(l):
    [3,4,5]
    if we run this code:
    >>>l = [1,2,3,4,5]
    >>>mystery_10(l)
    name 'limit' is not defiend
    '''
    l = []
    for e in list_of_number:
        if e > limit :
            l.append(e)
    return l
print(mystery_10([1,2,3,4,5])) 