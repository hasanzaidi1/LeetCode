

def count_code(str):
    wordCount = 0
    for i in range(len(str)):
        fourLetters = str[i:i+4]
    
        if fourLetters[0:2] == "co" and fourLetters[-1] == "e":
            wordCount += 1
    return wordCount

    