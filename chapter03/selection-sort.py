# 선택 정렬 예제
# 주어진 list 자체를 수정


def selectionSort(numList):

    n = len(numList)

    for i in range(0, n - 1):  # n과 n+1을 비교하기 때문에 마지막 index는 비교 할 필요가 없음

        currentIndex = i
        changeIndex = i

        for compareIndex in range(i + 1, n):

            if numList[compareIndex] < numList[currentIndex]:

                changeIndex = compareIndex

        # currentIndex를 ChangeIndex로 변경 , changeIndex를 currentIndex로 변경 =  numList[changeIndex], numList[currentIndex]

        numList[currentIndex], numList[changeIndex] = numList[
            changeIndex], numList[currentIndex]


numList = [1, 4, 2, 5, 9]

selectionSort(numList)

print(numList)
