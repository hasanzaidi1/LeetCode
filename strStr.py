
def strStr(haystack, needle):
    i = 0
    comp_word = []
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            comp_word = haystack[i:i+len(needle)]
            if (comp_word == needle):
                return i
    return(-1)


print(strStr(haystack = "sadbutsad", needle = "sad"))
print(strStr(haystack = "leetcode", needle = "leeto"))
