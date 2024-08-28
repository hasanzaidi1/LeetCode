def longestCommonPrefix(strs):

    shortestWordLen = min(map(len, strs))
    j = 0
    while j <= shortestWordLen:
        prefix = strs[0][:j + 1]
        for words in strs:
            currLetter = ""
            currLetter += words[:j+1]

            if currLetter == prefix:
                continue
            else:
                if j == 0:
                    return ""
                    break
                else:
                    return prefix[:j]

        j += 1

    return prefix



