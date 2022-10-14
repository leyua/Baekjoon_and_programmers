import sys
input = sys.stdin.readline

a, b = input().split()
a,b=a[::-1],b[::-1]
print(a if int(a) > int(b) else b)