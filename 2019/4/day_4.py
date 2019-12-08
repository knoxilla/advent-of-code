#!/usr/bin/env python3

pw_range = range(278384,824795)
print(pw_range[0], pw_range[-1], len(pw_range))
print()

slimmed = []
for p in pw_range:
   s = str(p)
   ok = True
   for i in range(5):
      if int(s[i]) > int(s[i+1]):
         ok = not ok
         break
   if ok:
      slimmed.append(p)

print(len(slimmed))
print(slimmed[0:9])
print(slimmed[-9:])
print()

from itertools import groupby

trimmed = []
for s in slimmed:
   s = str(s)
   ok = False
   groupers = ','.join(''.join(group) for key, group in groupby(s))
   # print(groupers)
   for group in groupers.split(','):
      if(len(group)) == 2:
         # print(group)
         ok = True
         break
   if ok:
      trimmed.append(s)

print(len(trimmed))
print(trimmed[:9])
print(trimmed[-9:])
print()
