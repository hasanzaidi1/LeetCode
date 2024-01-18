def isSubsequence( s, t):

  SList = []
  TList = []
  
  for itemS in s:
      SList.append(itemS)
  for itemT in t:
      TList.append(itemT)
  
  for alphS in SList:
      for alphT in TList:
          if alphS != alphT:
            TList.remove(alphT)
          else:
            continue
          
  
  return(TList==SList)


print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("ab", "baab")) # Should be true
  