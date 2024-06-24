
def maxProduct(words):
    currWrdLen = 0
    follWordLen = 0
    mxCtWrd = ''
    for i in range(len(words)):
        currWrd = words[i]
        currWrdLen = len(currWrd)
        follwWrd = words[i+1]
        follWordLen = len(follwWrd)
        if follWordLen > currWrdLen:
            mxCtWrd += follwWrd
        elif currWrdLen > follWordLen:
            mxCtWrd += currWrd
        return currWrdLen