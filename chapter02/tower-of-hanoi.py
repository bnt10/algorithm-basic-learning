#하노이의 탑 구현


def hanoi(frm, to, n, count):

    if n == 1:
        print(f'{frm} {to} ')
        return 1
    else:
        empty = 6 - frm - to
        count += hanoi(frm, empty, n - 1, count)
        print(f'{frm} {to}')
        count += hanoi(empty, to, n - 1, count)

    return count


print('원반의 개수: ')
numberOfDisk = int(input())
print('원반들의 시작 위치: ')
startLocation = int(input())
print('옮겨야 할 위치: ')
desLocation = int(input())
print('\n')
totalCount = hanoi(startLocation, desLocation, numberOfDisk, 0)
print(f'총 이동 횟수: {totalCount}')
