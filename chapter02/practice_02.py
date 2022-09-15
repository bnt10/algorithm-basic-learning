# 숫자 n개 중에서 최댓값 찾기를 재귀 방식으로 구현

numList = [1, 3, 8, 100, 10, 11, 9]
maxValue = numList[0]


def getMaxValue(numLength, maxValue):
    numLength = numLength - 1
    if numLength < 1:
        return maxValue
    maxValue = maxValue if maxValue >= numList[numLength] else numList[
        numLength]

    maxValue = getMaxValue(numLength, maxValue)
    return maxValue


print(getMaxValue(len(numList), maxValue))
