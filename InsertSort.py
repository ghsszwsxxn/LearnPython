def insert_sort(list):
    ans = []
    if len(list) == 0 or list is None:
        return ans
    ans.append(list[0])
    for l in list[1:]:
        for i, a in enumerate(ans):
            if l < a:
                ans.insert(i, l)
                break
        if l >= ans[-1]:
            ans.append(l)
    return ans

def insert_sort_v2(list):
    for i,l in enumerate(list):
        for j,a in enumerate(list[:i]):
            if l < a:
                target = l
                list[j+1:i+1] = list[j:i]
                list[j] = target
                break
    return list

list = [2,1,3,4,2,9,5,3]
#print(insert_sort(list))
print(insert_sort_v2(list))
