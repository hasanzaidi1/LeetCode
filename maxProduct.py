def maxProduct(words):

    sorted_list = sorted(words, key=len, reverse=True)
    max_sum = 0
    for i in range(len(sorted_list)-1):
        first_word_len = len(sorted_list[i])
        second_word_len = len(sorted_list[i+1])
        if first_word_len == second_word_len and have_no_common_chars(sorted_list[i], sorted_list[i+1]):
            max_sum = len(sorted_list[i]) * len(sorted_list[i+1])
            return max_sum
        else:
            continue

    return max_sum


def have_no_common_chars(word1,word2):

    set1 = set(word1)
    set2 = set(word2)

    if set1.isdisjoint(set2):
        return True
    else:
        return False

print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(maxProduct(["a","aa","aaa","aaaa"]))
