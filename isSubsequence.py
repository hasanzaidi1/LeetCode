
def isSubsequence(t, s):

  newList = []

  for letter_in_t in t:
    for letter_in_s in s:
      if letter_in_s == letter_in_t:
        newList.append(letter_in_s)
        s = chop_array_until_item(s,letter_in_s) 

  #compare s with updated t.list
  if list(t) == newList:
    return True
  else:
    return False


def chop_array_until_item(arr, item):
    if item in arr:
        index = arr.index(item)  # Find the index of the item
        chopped_array = arr[index+1:]  # Slice the array until that index
        return chopped_array
    else:
        return arr  # If the item is not found, return the original array


      