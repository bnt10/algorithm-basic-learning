#선택정렬
"""
given :
  numList = [1, 5, 3, 9, 7]

when :
  selectionSort(numList) # numList를 선택정렬을 구현한 함수에 인자로 전달

then :
  numList === [1, 3, 5, 7, 9] 오름 차순위로 정렬되어야 한다

"""


def sortingIndex(x, i, j):

    x[i], x[j] = x[j], x[i]


def selectionSort(numList):
    n = len(numList)
    for currentIndex in range(0, n - 1):
        changeIndex = currentIndex

        #currentIndex를 기준으로 전체 list를 비교하여 가장 작은 값의 index를 구한다.
        for compareIndex in range(currentIndex + 1, n):
            if numList[compareIndex] < numList[currentIndex]:
                changeIndex = compareIndex

        sortingIndex(numList, currentIndex, changeIndex)


numList = [1, 5, 3, 9, 7]

selectionSort(numList)
print(numList)
