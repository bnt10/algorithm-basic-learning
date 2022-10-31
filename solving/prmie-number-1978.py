n = int(input())

m = list(map(int, input().rstrip().split()))

count = 0
for num in m:
    if num > 1:
        i = 2
        check = True
        while i <= num**(1 / 2):

            if num % i == 0:
                check = False
            i += 1
        if check:
            count += 1
print(count)
