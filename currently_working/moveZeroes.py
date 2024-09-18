def moveZeroes(nums):
    
    list_zeroes = []
    for num in nums:

        if num == 0:
            list_zeroes.append(0)
            nums.remove(num)
        else:
            continue
    for zeroes in list_zeroes:
        nums.append(zeroes)

    return nums
    


print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0]))
print(moveZeroes([0,0,1]))
print(moveZeroes([1,0,1]))

