def sumByRecursion(n):
    if n < 1:
        return n
    n = n + sumByRecursion(n - 1)
    return n


if __name__ == '__main__':
    result = sumByRecursion(3)
    print(result)
