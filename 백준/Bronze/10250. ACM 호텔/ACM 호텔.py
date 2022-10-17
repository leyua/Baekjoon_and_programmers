import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    room = str(n % h if n % h != 0 else h)
    if (n - 1) // h + 1 < 10:
        room += "0"
    room += str((n - 1) // h + 1)
    print(room)