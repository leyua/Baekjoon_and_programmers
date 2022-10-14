import sys
input = sys.stdin.readline

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

def recursion(s, l, r):
    global n
    n += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)

t = int(input())
for _ in range(t):
    n = 0
    print(isPalindrome(input().strip()), n)