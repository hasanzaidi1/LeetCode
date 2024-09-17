

def romanToInt(s):
    hashTable = {
        'I':             1,
        'V':             5,
        'X':             10,
        'L':             50,
        'C':             100,
        'D':             500,
        'M':             1000
    }

    sum = 0
    s_list = list(s)

    for i in range(len(s_list)):
        pair = False
        if i > 0:
            # check if i lesser than i-1, if not then take them as a pair
            curr = hashTable[s_list[i]]
            prev = hashTable[s_list[i-1]]
            pair = curr > prev
            # print("curr Val :",hashTable[s_list[i]])
            # print("prev Val :",hashTable[s_list[i-1]])
            # print("SUM: ", sum)

        if pair:
            sum += hashTable[s_list[i-1]]-hashTable[s_list[i]]
        else:
            sum += hashTable[s_list[i]]
    return sum


print(romanToInt("LVIII"))
print(romanToInt("III"))
print(romanToInt("MCMXCIV"))

