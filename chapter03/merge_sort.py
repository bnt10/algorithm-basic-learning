sublist = [1, 2, 3, 7, 11, 33, 55, 22, 44, 13]


def mergeSort(list):
    breakPoint = len(list) <= 1
    if breakPoint: return list

    mid = len(list) // 2
    leftList = mergeSort(list[:mid])
    rightList = mergeSort(list[mid:])

    merged = merge(leftList, rightList)
    return merged


def merge(leftList, rightList):
    merged = []
    while len(leftList) > 0 and len(rightList) > 0:
        if leftList[0] <= rightList[0]:
            merged.append(leftList.pop(0))
        else:
            merged.append(rightList.pop(0))

    if len(leftList) > 0:
        merged += leftList
    if len(rightList) > 0:
        merged += rightList

    return merged


sorted = mergeSort(sublist)
print(sorted)
