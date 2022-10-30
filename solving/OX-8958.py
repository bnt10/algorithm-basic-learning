import sys

input = sys.stdin.readline

summationList = []
for i in range(int(input())):
    answerList = list(map(str, input().strip()))

    score = 0
    tmp = 0
    for answer in answerList:
        if answer == 'O':
            tmp = tmp + 1
            score += tmp
        else:
            tmp = 0
    summationList.append(score)

for i in summationList:
    print(i)
