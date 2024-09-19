

def isMatch(s, p):
    new_arr = []
    s_list = list(s)
    for index in range(len(p)):
        
        if p[index] == '.':
            s_list = s_list[:index]
            break

        if p[index] == '*':
            previous_char = p[index-1]
            new_arr.append(previous_char)
            continue
        new_arr.append(p[index])

    return(new_arr==s_list)
            


print(isMatch(s = "aa", p = "a*"))
print(isMatch(s = "aa", p = "a"))
print(isMatch(s = "ab", p = ".*"))
print(isMatch(s = "mississippi", p = "mis*is*p*."))





    # if '.' and '*'in p:
    #         print('.*')
    #         return True
    #     elif '*' in p:
    #         # check if the preceding letters in p are same as the exact amount of letters in s
    #         return True
    #         print('*')
    #     else:
    #         return s == p
            
    #     return False