
'''
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

'''


def xyz_there(str):

    for i in range(len(str)):
        if str[i] == 'x':
            if str[i:i+3] == "xyz" and str[i-1] != ".":
                return True
            else:
                continue
            
    return False
