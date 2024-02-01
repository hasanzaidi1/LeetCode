
def isSubsequence( s, t):

  SList = []
  TList = []
  
  for itemS in s:
    SList.append(itemS)
  for itemT in t:
    TList.append(itemT)
  
  print()
  print(TList)
  print(SList)
  print()

  
  for alphS in SList:
    for alphT in TList:
      if alphS == alphT:
        continue
      else:
        TList.remove(alphT)
    # SList.remove(alphS)
        

  print(TList)
  
  given_s = list(s)
  print(given_s)
  return(TList==given_s)






