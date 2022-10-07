a, b, c = map(int, input().split())
if a == b == c:
    print(10000+a*1000)
elif a == b or b == c or c == a:
    for i in a, b, c:
        if [a, b, c].count(i) == 2:
            print(1000+i*100)
            break
else:
    print(max(a, b, c)*100)