def isUgly(n):
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False
    
print(isUgly(6))