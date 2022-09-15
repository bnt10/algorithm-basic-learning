#1부터 n까지의 합을 재귀로 구현


def sumByRecursion(n):
    if n < 1:
        return n
    n = n + sumByRecursion(n - 1)
    return n


result = sumByRecursion(3)
print(result)
# 3 -> 2 -> 1
# 0 + 1 + 2 + 3 
