def isSubsequence( s, t):

  result = []
  SList = []
  TList = []
  
  for itemS in s:
      SList.append(itemS)
  for itemT in t:
      TList.append(itemT)
  
  for alphT in TList:
      for alphS in SList:
          if alphS != alphT:
              continue
          else:
              if alphT not in result:
                  result.append(alphT)
                  SList.remove(alphS)
  
  result = ''.join(result)
  print(TList)
  print(SList)
  
  return(result==s)


print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("ab", "baab"))
  