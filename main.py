import isSubsequence as iS
import removeDuplicates as rD
import countHi as ch
import cat_dog as cd
import count_code as cc
import end_other as eo
import xyz_there as xy
import maxProduct as mp

print()
print()
print("isSubsequence")
print()

print(iS.isSubsequence("abc","ahbgdc"))
print(iS.isSubsequence("axc","ahbgdc"))
print(iS.isSubsequence("ab","baab")) # Should be true
print(iS.isSubsequence("abc","abc")) # Should be true

print()
print()
print("removeDuplicates")
print()

print(rD.removeDuplicates([1,1,2222,2,2,2]))
print(rD.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(rD.removeDuplicates([0,11,2,2,2,2,2,2,2,2,2,2,2,2]))

print()
print()
print("countHi")
print()

print(ch.count_hi('abc hi ho'))
print(ch.count_hi('hiHIhi'))
print(ch.count_hi('hihi'))
print(ch.count_hi('hi'))
print(ch.count_hi('ABChi hi'))
print(ch.count_hi(''))
print(ch.count_hi('Hi is no HI on ahI'))

print()
print()
print("cat_dog")
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

print()
print()
print("count_code")
print()

print(cc.count_code('aaacodebbb'))
print(cc.count_code('codexxcode'))
print(cc.count_code('cozexxcope'))
print(cc.count_code('cozfxxcope'))
print(cc.count_code('xxcozeyycop'))
print(cc.count_code('abcxyz'))
print(cc.count_code('code'))
print(cc.count_code('ode'))
print(cc.count_code('AAcodeBBcoleCCccoreDD'))

print()
print()
print("end_other")
print()

print(eo.end_other('Hiabc', 'abc'))
print(eo.end_other('AbC', 'HiaBc'))
print(eo.end_other('abc', 'abXabc'))

print()
print()
print("xyz_there")
print()

print(xy.xyz_there('abcxyz'))
print(xy.xyz_there('abc.xyz'))
print(xy.xyz_there('xyz.abc'))
print(xy.xyz_there('xyz'))
print(xy.xyz_there('xy'))
print(xy.xyz_there('abc.xyzxyz'))
print(xy.xyz_there('abc.xxyz'))
print(xy.xyz_there('12xyz'))



print()
print()
print("maxProduct")
print()


print(mp.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(mp.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(mp.maxProduct(["a","aa","aaa","aaaa"]))
