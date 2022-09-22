# numberList에서 중복된 값들에 대한 targetIndexList 만들기


def getTargetList(numberList, targetValue):

    targetIndexList = []
    for index in range(0, len(numberList)):
        if targetValue == numberList[index]:
            targetIndexList.append(index)

    if targetIndexList:
        print(f'찾고자 하는 targetValueIndexList : {targetIndexList}')
    else:
        print("찾고자 하는 값이 존재하지 않습니다.")


numberList = [1, 3, 3, 5]
getTargetList(numberList, 3)
getTargetList(numberList, 11)
