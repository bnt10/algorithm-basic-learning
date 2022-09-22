# 삽입 정렬


def insertSort(numList):
    n = len(numList)
    for i in range(1, n):
        insertValue = numList[i]

        compareIndex = i - 1  # insertValue의 바로 이전값

        while compareIndex >= 0 and numList[compareIndex] > insertValue:
            #compareIndex의 value가 더 큰 경우의 값을 바로 다음 값 위치로 변경
            numList[compareIndex + 1] = numList[compareIndex]
            #compareIndex의 앞 값들을 비교하기 위해서 index를 하나씩 감소
            compareIndex -= 1
        numList[compareIndex + 1] = insertValue


numList = [4, 2, 5, 1, 3, 9, 7]
insertSort(numList)
print(numList)
