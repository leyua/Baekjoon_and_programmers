import sys
input = sys.stdin.readline

s = input().strip()
n = 0
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for a in croatia:
    n += s.count(a)
print(len(s) - n)