# 회문판단 Queue
"""
given :
  noPalindromeSentence = '기찻길'
  yesPalindromeSentence = '역삼역'

when :
  print(checkPalindromeWithQueue(noPalindromeSentence))  
  print(checkPalindromeWithQueue(yesPalindromeSentence))

then :    
  queue을 이용해 구현 되어야 하며  
  반환값은 False, True가 되어야 한다 

"""


def checkPalindromeWithQueue(sentence):

    queue = []
    reversedQueue = []
    for s in sentence:
        queue.append(s.lower())

    for s in reversed(sentence):
        reversedQueue.append(s.lower())
    
    while queue:
        if queue.pop(0) != reversedQueue.pop(0):
            return False

    return True

noPalindromeSentence = '기찻길'
yesPalindromeSentence = '역삼역'

print(checkPalindromeWithQueue(noPalindromeSentence))
print(checkPalindromeWithQueue(yesPalindromeSentence))
