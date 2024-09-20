def isUgly(n):
    ugly_pf = [2,3,5]
    if n == 1:
        return True
    if n == 0:
        return False
    while n % 2 == 0 and n not in ugly_pf:
        n = n/2
    while n % 3 == 0 and n not in ugly_pf:
        n = n/3
    while n % 5 == 0 and n not in ugly_pf:
        n = n/5

        
    if n in ugly_pf:
        return True
    return False
        

   
print(isUgly(6))
print(isUgly(1))
print(isUgly(14))
print(isUgly(27))

