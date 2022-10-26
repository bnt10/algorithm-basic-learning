n, x = map(int,input().split())
numList = list(map(int,input().split()))
find_numbers = [str(i) for i in numList if i < x]
print(" ".join(find_numbers))
