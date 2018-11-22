from linked_list import *
"""
del
extend
"""

def test_list(builtin_list):
    l1 = Linkedlist(builtin_list)
    print("constructor:")
    print(l1)
    
    l2 = Linkedlist([])
    for e in builtin_list:
        l2.append(e)
    print("append:")
    print(l2)
    
    l3 = l1.copy()
    print("copy:")
    print(l3)
    
    l1.reverse()
    print("reverse:")
    print(l1)
    
    print("get:")
    for i in range(len(l2)):
        print(l2[i], end='')
        
    for i in range(len(l2)):
        l2[i] = i
    print("set:")
    print(l2)
    
    print("sort")
    for meth in [Linkedlist.insertion_sort, Linkedlist.selection_sort, Linkedlist.bubble_sort]:
        l = Linkedlist(builtin_list)
        meth(l)
        print(l)

    print("delete:")
    l4 = Linkedlist(builtin_list)
    for i in range(len(builtin_list)):
        del l4[0]
        print(l4)

    print("extend:")
    l5 = Linkedlist(builtin_list)
    l5.extend(builtin_list) ## should extend by a linked list
    print(l5)
print("\n\nempty")
test_list([])
print("\n\nsingle")
test_list(["a"])
print("\n\nsorted")
test_list(["a","b","c","d","e"])
print("\n\nreversed")
test_list(["e","d","c","b","a"])
print("\n\nunsorted")
test_list(["e","c","d","a","b"])
