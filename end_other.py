'''

Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True

'''



def end_other(a, b):

    if len(a) > len(b):
        startingInd = len(a) - len(b)
        if a[startingInd:].lower() == b.lower():
            return True
        else:
            return False
    
    elif len(b) > len(a):
        startingInd = len(b) - len(a)
        if b[startingInd:].lower() == a.lower():
            return True
        else:
            return False
        
    else:
        startingInd = 0
        if b[startingInd:].lower() == a.lower():
            return True
        else:
            return False
        

