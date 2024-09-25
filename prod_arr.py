
def productExceptSelf(nums):
        len_nums = len(nums)
        new_arr = [1] * len_nums  # Initialize the output array with 1s

        # Step 1: Calculate prefix products
        prefix_product = 1
        for i in range(len_nums):
            new_arr[i] = prefix_product
            prefix_product *= nums[i]

        # Step 2: Calculate suffix products
        suffix_product = 1
        for i in range(len_nums - 1, -1, -1):  # Loop backwards through the array
            new_arr[i] *= suffix_product  # Multiply the current value with the suffix product
            suffix_product *= nums[i]  # Update the suffix product

        return new_arr
    
    






print(productExceptSelf(nums = [1,2,3,4]))
print(productExceptSelf(nums = [-1,1,0,-3,3]))
print(productExceptSelf(nums = [1,-2,3,-4,5]))
