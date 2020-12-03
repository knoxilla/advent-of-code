#!/usr/bin/env python3

with open("report", "r") as f:
    info = f.read().splitlines()

entries = [int(i) for i in info]
entries.sort()

# first way, a bit naive, loops too much!
x = 0
for a in entries:
    for b in reversed(entries):
        x += 1
        if a + b == 2020:
            print(a, b, a * b)
            break

print(x)
print("")

# https://nedbatchelder.com/blog/201608/breaking_out_of_two_loops.html

# second way, with generators!
# would work better with a bigger list
# makes the 'get out of two loops' issue go away


def pairs(entries):
    for i in entries:
        for j in reversed(entries):
            yield i, j


y = 0
for a, b in pairs(entries):
    y += 1
    if a + b == 2020:
        print(a, b, a * b)
        break

print(y)
print("")

print(f"Notice that {y} is much less than {x}. Boom!")
