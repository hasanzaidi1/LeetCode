
def sortByBits(arr):
    return sorted(arr, key=lambda num: (countBits(num), num))

    
    

def countBits(num):
    return bin(num).count('1')