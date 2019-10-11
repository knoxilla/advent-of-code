#!/usr/bin/env python

file = open('blocks')
for line in file:
    blocks = map(int, line.split("\t") )

seen = []
while blocks not in seen:
    seen.append(list(blocks))
    frombank, tomove = max(enumerate(blocks), key=lambda item: item[1])
    blocks[frombank] = 0
    for item,blk in enumerate(range(tomove)):
        blocks[(frombank+1+item) % 16] += 1
    #if list(blocks) in seen:
    #    print ""
    #    print blocks
    #    break

print ""
print len(seen)
print seen.index(list(blocks))
print ""
print seen[seen.index(list(blocks))]
print ""
print len(seen) - seen.index(list(blocks))
