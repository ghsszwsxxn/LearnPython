def find_min(list):
    index = 0
    if len(list) == 0 or list is None:
        return None
    for i in range(len(list)-1):
        if list[i+1] < list[index]:
            index = i+1
    return index


def swap(list,index_a, index_b):
    tmp = list[index_a]
    list[index_a] = list[index_b]
    list[index_b] = tmp


def choose_sort(list):
    if len(list) == 0 or list is None:
        return list
    for i in range(len(list)-1):
        l = list[i]
        min = find_min(list[i:])
        if list[min+i] < l:
            swap(list,min+i, i)
    return list

#list = [5,4,3,2,1]
#print(find_min(list))
list = [2, 3, 4, 1, 4, 5, 68, 6, 9]
print(choose_sort(list))
