import sys


def wordSort():
    word = set()
    for i in range(int(input())):
        word.add(sys.stdin.readline().rstrip())

    wordList = list(word)
    wordList.sort()  # Sort alphabetically
    print(wordList)['a', 'b', 'c', 'b']

    wordList.sort(key=lambda x: len(x))  # Sort by character length

    print('\n'.join(wordList))


wordSort()
