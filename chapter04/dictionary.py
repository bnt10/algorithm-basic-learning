"""
given :
  studentDict = {
      39: 'Justin',
      14: 'John',
      67: 'Mike',
      105: 'Summer',
  }

when :
  print(findNameById(39))  

then : 
  key가 존재하는경우 return true
  그렇지 않으면 false
"""
studentDict = {
    39: 'Justin',
    14: 'John',
    67: 'Mike',
    105: 'Summer',
}


def findNameById(key):
    if key in studentDict:
        return True

    return False


#print(findNameById(39)) # true
print(findNameById(20))  # false
