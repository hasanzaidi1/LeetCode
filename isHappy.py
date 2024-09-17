

def isHappy(n):
    
    nums_return = []
    while n != 1 and n not in nums_return:
        nums_return.append(n)
        n = findSum(n)
    return n == 1

    

def findSum(n):
    sum = 0
    for num_chars in str(n):
        sum += int(num_chars) ** 2
    return sum


print(isHappy(19))
print(isHappy(9))
