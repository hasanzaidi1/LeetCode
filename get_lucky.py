


def getLucky(s, k):
    summ = 0
    char_list = s.strip().lower()
    list_num = []
    for chars in char_list:
        alpha_order = ord(chars) - ord('a') + 1
        ac = str(alpha_order)

        if len(ac) > 1:
            for n in ac:
                list_num.append(int(n))
        else:
            list_num.append(alpha_order)

    summ += count_sum(list_num, k)

    return summ

def count_sum(num_list, k):
    sum = 0
    while k != 0:
        sum = 0
        for num in num_list:
            sum += int(num)
        num_list = str(sum)
        k-=1

    return sum



print(getLucky(s = "zbax", k = 2))
print(getLucky(s="iiii", k=1))
print(getLucky(s="leetcode", k=2))

