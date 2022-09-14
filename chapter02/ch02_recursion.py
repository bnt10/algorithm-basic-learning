def recursion(n):
    n = n - 1

    print("recursion!!")
    if n > 0:  # RecursionError 를 막기 위한 조건
        recursion(n)  # recursion() 함수 안에서 다시 recursion()를 호출


if __name__ == '__main__':
    recursion(3)  # recursion( ) 함수를 호출
