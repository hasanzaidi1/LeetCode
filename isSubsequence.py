
def isSubsequence(t, s):

  newList = []

  for letter_in_t in t:
    for letter_in_s in s:
      if letter_in_s == letter_in_t:
        newList.append(letter_in_s)
        index = s.index(letter_in_s)  
        s = s[index+1:]
        break

  #compare s with updated t.list
  if list(t) == newList:
    return True
  else:
    return False


      