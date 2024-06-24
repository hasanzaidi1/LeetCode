
def maxProduct(words):
    biggestWord = findMaxCntChrs(words)
    return biggestWord


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