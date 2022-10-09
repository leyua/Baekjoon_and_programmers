import sys
input = sys.stdin.readline

n, x = map(int, input().split())
values = list(filter(lambda i: i < x, map(int, input().split())))
print(str(values).strip("[]").replace(",", ""))