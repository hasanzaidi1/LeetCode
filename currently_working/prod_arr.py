
def productExceptSelf(nums):


    new_arr = [0] * len(nums)
    prod = 1
    j = 0
    while j <= len(nums)-1:
        for i in range(len(nums)):
            if i == j:
                continue
            prod *= nums[i]

        new_arr[j] = prod
        prod = 1
        j += 1
    

    return new_arr

print(productExceptSelf(nums = [1,2,3,4]))
print(productExceptSelf(nums = [-1,1,0,-3,3]))