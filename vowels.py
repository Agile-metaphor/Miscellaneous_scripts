vowels = ['a','e','i','o','u','y', ' ']
import os
total = 16456
l = 0
# from itertools import permutations
# for p in permutations('kdkmpaeiou y'):
#     with open('./sum.txt', 'a+', encoding="utf-8") as fp:
#         fp.write(str(''.join(p)))
#         fp.write('\n')
#         fp.close()
#     print(str(i) + " out of " + str(total))
#     i+=1
first = ["k"] 
second = vowels
cc = ["d"]
dd = vowels
ee = ["k"]
ff = vowels
gg = ["m"]
hh = vowels
ii = ["p"]
jj = vowels

for f in first: 
    for s in second: 
        for c in cc:
            for d in dd:
                for e in ee:
                    for f in ff:
                        for g in gg:
                            for h in hh:
                                for i in ii:
                                    for j in jj:
                                            with open('./sum.txt', 'a+', encoding="utf-8") as fp:
                                                fp.write(f + s + c + d + e + f + g + h + i + j)
                                                fp.write('\n')
                                                fp.close()
                                            print(str(l) + " out of " + str(total))
                                            l+=1