import isSubsequence as iS
import removeDuplicates as rD
import countHi as ch
import cat_dog as cd

print()

print(iS.isSubsequence("abc","ahbgdc"))
print(iS.isSubsequence("axc","ahbgdc"))
print(iS.isSubsequence("ab","baab")) # Should be true
print(iS.isSubsequence("abc","abc")) # Should be true

print()

print(rD.removeDuplicates([1,1,2222,2,2,2]))
print(rD.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(rD.removeDuplicates([0,11,2,2,2,2,2,2,2,2,2,2,2,2]))

print()

print(ch.count_hi('abc hi ho'))
print(ch.count_hi('hiHIhi'))
print(ch.count_hi('hihi'))
print(ch.count_hi('hi'))
print(ch.count_hi('ABChi hi'))
print(ch.count_hi(''))
print(ch.count_hi('Hi is no HI on ahI'))

print()

print(cd.cat_dog('catdog'))
print(cd.cat_dog('catcat'))
print(cd.cat_dog('1cat1cadodog'))
print(cd.cat_dog('catxxdogxxxdog'))
print(cd.cat_dog('catxdogxdogxcat'))
print(cd.cat_dog('catxdogxdogxca'))
print(cd.cat_dog('dogdogcat'))
print(cd.cat_dog('dogogcat'))
print(cd.cat_dog('dog'))
print(cd.cat_dog('cat'))




