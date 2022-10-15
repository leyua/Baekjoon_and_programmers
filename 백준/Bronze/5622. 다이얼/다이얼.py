s = input()
t = 0
a = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
for alphabet in s:
    for i in range(len(a)):
        if alphabet in a[i]:
            t += i + 3
print(t)