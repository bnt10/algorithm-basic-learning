inputRaw = int(input())

for _ in range(inputRaw):

    data = scoreList = list(map(int, input().split()))
    personnel = data[0]
  
    sum_value = sum(i for i in data[1:])
    avg = sum_value / personnel
    count = 0
    for i in data[1:]:
        if i > avg:
            count += 1

    print("%.3f%%" % (count / personnel * 100))
