# 숫자 n개 중에서 최댓값 찾기를 재귀 방식으로 구현

numList = [1, 3, 5, 6]
maxValue = numList[0]
def getMaxValue(numLength,maxValue):
  numLength = numLength - 1
  if numLength < 1:
    return maxValue
  maxValue = maxValue if maxValue >= numList[numLength]  else numList[numLength]
  getMaxValue(numLength,maxValue)
  return maxValue
    
print(getMaxValue(len(numList),maxValue))