def insertSort(numList):
    for i in range(1, len(numList)):
        insertValue = numList[i]
        compareIndex = i - 1

        while compareIndex >= 0 and numList[compareIndex] > insertValue:
            numList[compareIndex + 1] = numList[compareIndex]
            compareIndex -= 1
        numList[compareIndex + 1] = insertValue

    for i in numList:
        print(i)


totalNum = int(input())
numList = [int(input()) for i in range(totalNum)]
insertSort(numList)
