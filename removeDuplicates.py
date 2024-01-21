def removeDuplicates(nums):
  uniqueNums = []
  
  for num in nums:

    if num not in uniqueNums:
      uniqueNums.append(num)

    else:
      continue

  return uniqueNums
