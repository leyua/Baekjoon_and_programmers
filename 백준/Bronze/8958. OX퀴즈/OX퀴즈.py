import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    ox = input()
    value = 0
    total = 0
    for j in ox:
        if j == "O":
            value += 1
        else:
            value = 0
        total += value
    print(total)