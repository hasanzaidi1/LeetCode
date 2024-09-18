
def moveZeroes(nums):
    
    non_zero_index = 0  

    for current in range(len(nums)):
        if nums[current] != 0:
            temp = nums[non_zero_index]
            nums[non_zero_index] = nums[current]
            nums[current] = temp

            non_zero_index += 1  
    
    return nums
    


print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0]))
print(moveZeroes([0,0,1]))
print(moveZeroes([1,0,1]))

