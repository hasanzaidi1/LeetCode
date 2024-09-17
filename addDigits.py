def addDigits(num):
    str_num = str(num)
    
    while len(str_num) != 1:
        sum = 0
        for nums in str_num:
            sum += int(nums)
        str_num = str(sum)
    return int(str_num)

print(addDigits(38))