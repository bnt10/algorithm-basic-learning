#피보나치 수열을 재귀 방식으로 구현


def fibonacci(n):
    if n <= 1:
        return n

    n = fibonacci(n - 2) + fibonacci(n - 1)
    return n


print(fibonacci(7))
