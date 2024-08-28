
def isPalindrome(x):
    x_str = str(x)
    list_forward = []
    list_backward = []
    for each_num in x_str:
        list_forward.append(each_num)

    for each_num in x_str[::-1]:
        list_backward.append(each_num)

    if list_forward == list_backward:
        return True
    else:
        return False


print(isPalindrome(121))