import sys
input = sys.stdin.readline

s = input()
n = []
for alphabet in "abcdefghijklmnopqrstuvwxyz":
    n.append(str(s.find(alphabet)))
print(" ".join(n))