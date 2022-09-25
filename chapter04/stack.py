# 회문판단 Stack
"""
given :
  noPalindromeSentence = '기찻길'
  yesPalindromeSentence = '역삼역'

when :
  print(checkPalindromeWithStack(noPalindromeSentence))  
  print(checkPalindromeWithStack(yesPalindromeSentence))

then :    
  stack을 이용해 구현 되어야 하며  
  반환값은 False, True가 되어야 한다 

"""


def checkPalindromeWithStack(sentence):

    stack = []
    reversedStack = []
    for s in sentence:
        stack.append(s.lower())

    for s in reversed(sentence):
        reversedStack.append(s.lower())

    while stack:
        if stack.pop() != reversedStack.pop():
            return False

    return True


noPalindromeSentence = '기찻길'
yesPalindromeSentence = '역삼역'

print(checkPalindromeWithStack(noPalindromeSentence))
print(checkPalindromeWithStack(yesPalindromeSentence))
