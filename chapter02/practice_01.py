#1부터 n까지의 합을 재귀로 구현

def sumByRecursion(n):
    if n < 1:
        return n
    n = n + sumByRecursion(n - 1)
    return n


if __name__ == '__main__':
    result = sumByRecursion(3)
    print(result)
