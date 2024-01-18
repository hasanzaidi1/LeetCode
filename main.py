import isSubsequence as iS


print(iS.isSubsequence("abc", "ahbgdc"))
print(iS.isSubsequence("axc", "ahbgdc"))
print(iS.isSubsequence("ab", "baab")) # Should be true

print(iS.isSubsequence("abc", "abc")) # Should be true
