import sys
def countingSort(list):
  maxValue  = max(list)

  countingList = [0 for i in range(maxValue+1)]

  for i in list:
      countingList[i] += 1
 
  
  for i in range(1, maxValue + 1):
      countingList[i] += countingList[i - 1]

  result = [0] * len(list)
  
  for i in list:
      result[countingList[i] - 1] = i
      countingList[i] -= 1
  return result



n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
for i in countingSort(nums):
    sys.stdout.write(str(i)+'\n')