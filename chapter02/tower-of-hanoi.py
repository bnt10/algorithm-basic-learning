def hanoi(n, frm, to):
    if n > 1:
        hanoi(n - 1, frm, 6 - frm - to)  # 기둥이 1개 이상이면 그룹으로 묶인 n-1개 원판을
        # 중간으로 먼저 다 옮긴다

    print(frm, to)

    if n > 1:
        hanoi(n - 1, 6 - frm - to, to)


n = int(input())

print(2**n - 1)  #총 이동해야 하는 횟수
hanoi(n, 1, 3)

# n == 1
# 1 -> 3  = 1 번

# n == 2
# 1 -> 2  = 1번
# 1 -> 3  = 2번
# 2 -> 3  = 3번
