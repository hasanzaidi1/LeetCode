def maxProduct(words):

    bitmasks = []


    for word in words:
        bitmask = 0
        for char in word:
            bitmask |= 1 << (ord(char) - ord('a'))
        bitmasks.append(bitmask)

    max_product = 0
    n = len(bitmasks)

    for i in range(n):
        for j in range(i + 1, n):
            bmi = bitmasks[i]
            bin_bmi = bin(bmi)
            bmj = bitmasks[j]
            bin_bmj = bin(bmj)
            if bmi & bmj == 0:

                words_len_prod = len(words[i]) * len(words[j])
                max_product = max(max_product, words_len_prod)

    return max_product



print(maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))  # Output should be 16
print(maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))  # Output should be 16
print(maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))  # Output should be 4
print(maxProduct(["a", "aa", "aaa", "aaaa"]))  # Output should be 0
print(maxProduct(["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]))  # Output should be 15
