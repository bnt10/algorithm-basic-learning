#삽입정렬
"""
given :
  numList = [1, 5, 3, 9, 7]

when :
  insertSort(numList) # numList를 삽입정렬 구현한 함수에 인자로 전달

then :
  numList === [1, 3, 5, 7, 9] 오름 차순위로 정렬되어야 한다

"""


def insertSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
       
        while i > 0 and x[i - 1] > val:
            x[i] = x[i - 1]
            i -= 1
        x[i] = val
        print(x)


numList = [1, 5, 3, 9, 7]
insertSort(numList)
print(numList)
