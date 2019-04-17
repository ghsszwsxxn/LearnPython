import random


def quick_sort(list, left, right):
    if left >= right:
        return
    index = partition(list, left, right)
    quick_sort(list, left, index - 1)
    quick_sort(list, index + 1, right)


def partition(list, left, right):
    target_index = int(random.random() * (right - left + 1)) + left
    swap(list, left, target_index)
    target = list[left]

    while left < right:
        while left < right and target <= list[right]:
            right = right - 1
        swap(list, left, right)

        while left < right and target >= list[left]:
            left = left + 1
        swap(list, left, right)
    return left


def swap(list, index_a, index_b):
    if index_a == index_b:
        return
    tmp = list[index_a]
    list[index_a] = list[index_b]
    list[index_b] = tmp


def swap2(a, b):
    print(type(a))
    t = a
    a = b
    b = t
    print("swap2方法内部，a:{},b:{}".format(a, b))


list = [3, 5, 2, 7, 5, 9, 12, 23, 18]
quick_sort(list, 0, len(list) - 1)
print(list)

# a = "1"
# b = "2"
# swap2(a,b)
# print("方法外部：a:{},b:{}".format(a,b))
