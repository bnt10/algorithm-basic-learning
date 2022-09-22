# 순차검색 예제


def sequentialSearch(numberList, targetValue):

    # 입력: numberList:숫자 리스트, targetValue: 찾는값

    # 출력: numberList에서  targetValue 의 index

    for index in range(0, len(numberList)):  #전체 리스트를 순차적으로 비교
        if targetValue == numberList[index]:

            return print(f'targetValue의 Index {index}')  # targetValue의 index

    return print('해당값은 존재하지 않습니다.')  #값이 없는 경우


numList = [1, 2, 3, 4, 5]

sequentialSearch(numList, 3)

sequentialSearch(numList, 10)
