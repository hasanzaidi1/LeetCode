def cat_dog(str):
  isCat = 0
  isDog = 0
  for i in range(0,len(str)):
    if str[i:i+3] == "cat" or str[i:i+3] == "dog":
      if str[i:i+3] == "cat":
        isCat += 1
      if str[i:i+3] == "dog":
        isDog += 1
        
  if (isCat == isDog):
    return True
  else:
    return False
