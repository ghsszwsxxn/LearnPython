def bubble_sort(list):
    if len(list) == 0 or list is None:
        return list
    for i in range(len(list) - 1):
        for j, l in enumerate(list[:-i]):
            if l < list[j + 1]:
                swap(list[j], list[j+1])
        return list

def swap(a,b):
    c = a
    a = b
    b = c

list = [1, 2, 3, 2, 8, 6, 5, 6, 4]
print(bubble_sort(list))
