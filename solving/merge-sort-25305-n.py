

def mergeSort(list, start, end):
    if start >= end: return
    mid = (start + end) // 2
    mergeSort(list, start, mid)  # find left
    mergeSort(list, mid + 1, end)  # find right
    merge(list, start, mid + 1, end)


def merge(list, left, right, end):
    merged = []
    l, r = left, right
    while l < right and r <= end:
        if list[l] >= list[r]:
            merged.append(list[l])
            l += 1
        else:
            merged.append(list[r])
            r += 1
    while l < right:
        merged.append(list[l])
        l += 1
    while r <= end:
        merged.append(list[r])
        r += 1

    l = left
    for n in merged:
        list[l] = n
        l += 1


totalNum, limitCount = map(int, input().split())

numList = list(map(int, input().split()))

mergeSort(numList, 0, len(numList) - 1)
print(numList[limitCount - 1])
