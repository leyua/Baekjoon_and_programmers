import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r, s = input().split()
    p = "".join([i * int(r) for i in s])
    print(p)