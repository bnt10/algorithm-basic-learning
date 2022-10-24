import sys

input = sys.stdin.readline
N = input()

arr = list(map(int, input().split()))
arrSet = sorted(list(set(arr)))

dic = {arrSet[i]: i for i in range(len(arrSet))}

print(' '.join(str(dic[i]) for i in arr))
