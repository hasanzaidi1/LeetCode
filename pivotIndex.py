
def pivotIndex(nums):

    len_nums = len(nums)

    for i in range(len(nums)):
        pivot_ind = i
        left_arr = nums[0:pivot_ind]
        right_arr = nums[pivot_ind+1:len_nums]
        if sum(left_arr) == sum(right_arr):
            return i
    return -1


print(pivotIndex(nums = [1,7,3,6,5,6]))
print(pivotIndex(nums = [1,2,3]))
print(pivotIndex(nums = [2,1,-1]))
