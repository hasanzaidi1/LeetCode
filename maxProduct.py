
def maxProduct(words):
    maxWord = findMaxCntChrs(words)
    maxProd = 0
    for word in words:
        if word != maxWord and len(word) == len(maxWord): 
            maxProd = len(word) * len(maxWord)
        else:
            words.remove(maxWord)
            maxWord = findMaxCntChrs(words)
    return maxProd


def findMaxCntChrs(words):
    currWrd = ''
    mxCtWrd = words[0]
    for i in range(len(words)):
        currWrd = words[i]
        if len(currWrd) > len(mxCtWrd):
            mxCtWrd = currWrd
        else:
            continue
    return mxCtWrd