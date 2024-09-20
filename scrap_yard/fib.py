
def fib(n):
    result = 0
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)

    return result


def fib_btm_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3,n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[i]

# Recursion: 

    #              fib(5)
    #            /       \
    #        fib(4)      fib(3)          = result
    #       /     \       /     \
    #   fib(3)   fib(2) fib(2)  fib(1)   = result
    #     /  \      |     |       |
    # fib(2) fib(1) 1  +  1   +   1      = result
    #    |      |   |     |       |
    #    1   +  1 + 1  +  1   +   1      = result


print(fib(10))
print(fib_btm_up(500))
