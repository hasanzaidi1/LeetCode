
def maxProduct(words):
    maxWords = find2MaxCntWrds(words)
    return len(maxWords[0]) * len(maxWords[1])


def find2MaxCntWrds(words):
    mxCtWrd2 = ''

    while mxCtWrd2 == '' and len(words) != 0:

        mxCtWrd1 = findMax(words)
        words.remove(mxCtWrd1)
        
        for word in words:
            if len(word) == len(mxCtWrd1) and noCommonLetters(word,mxCtWrd1):     # maybe add into cond that word isnt the same
                mxCtWrd2 = word
                break
            else:
                continue

    return mxCtWrd1, mxCtWrd2


def findMax(words):

    mxCtWrd = words[0]
    for i in range(len(words)):
        currWrd = words[i]
        if len(currWrd) > len(mxCtWrd):
            mxCtWrd = currWrd
    return mxCtWrd



def noCommonLetters(word1,word2):

    # Convert both words to sets of characters
    set1 = set(word1)
    set2 = set(word2)

    # Check for intersection between the sets
    if set1 & set2:
        return False
    return True