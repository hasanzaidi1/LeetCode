def containsDuplicate(nums):

    sorted_nums = sorted(nums)
    len_nums = len(sorted_nums)
    contains_dup = False
    for i in range(len_nums-1):
        
        if sorted_nums[i] == sorted_nums[i+1]:
            contains_dup = True
            break
        else:
            continue

    return contains_dup

print(containsDuplicate([2,14,18,22,22]))
print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))

