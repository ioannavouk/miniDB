import math

def bin_search(x, list1, op):

    list_or = list1
    index_sort = sorted(range(len(list1)), key=lambda k:(list1[k] is None,  list1[k]))
    list_sort_none = sorted(list1, key=lambda x: (x is None, x))
    list_sort = []
    for val in list_sort_none:
        if val != None :
            list_sort.append(val)
    index_bin = []
    list_final = []
    bottom = 0
    top = len(list_sort)-1
    found = False
    location = -1
    while(bottom <= top) and not(found):
        middle = int((bottom + top)//2)
        if(list_sort[middle] == x):
            location = middle
            found = True
        else:
            if x < list_sort[middle]:
                top = middle - 1
            else:
                bottom = middle + 1
    # Index of last occurrence
    location_l = -1
    # Index of first occurrence
    location_f = -1

    # Finds last index that matches x
    for I in range(len(list_sort)):
        if list_sort[I] == x:
            location_l = I
    # Finds first index that matches x
    for I in range(len(list_sort)):
        if list_sort[I] == x:
            location_f = I
            break

    if location_f == -1:
        return 0
    else:
        if op == '==':
            bin_res =  list(range(math.ceil(location_f), math.ceil(location_l)+1))
        elif op == '>=':
            bin_res = list(range(math.ceil(location_f), math.ceil(len(list_sort))))
        elif op == '<=':
            bin_res = list(range(0, math.ceil(location_l)+1))
        elif op == '<':
            bin_res = list(range(0, math.ceil(location_l)))
        elif op == '>':
            bin_res = list(range(math.ceil(location_f)+1, math.ceil(len(list_sort))))


        for i in bin_res: index_bin.append(index_sort[i])



    return index_bin
