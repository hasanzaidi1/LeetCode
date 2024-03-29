'''

Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

'''

def count_hi(str):
  num_hi = 0
  for i in range(len(str)):
    twoLetters = str[i:i+2]
    if twoLetters == "hi":
      num_hi += 1
  return(num_hi)
