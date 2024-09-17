

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
    i = 0
    while i < len(s_list):
        pair = False
        if i < len(s_list)-1 and hashTable[s_list[i]] < hashTable[s_list[i+1]]:
            pair = True
        if pair:
            sum += hashTable[s_list[i+1]]-hashTable[s_list[i]]
            i += 1
        else:
            sum += hashTable[s_list[i]]
        i += 1
    return sum


print(romanToInt("LVIII"))
print(romanToInt("III"))
print(romanToInt("MCMXCIV"))
print(romanToInt("CMXCIV"))  # Output: 994


