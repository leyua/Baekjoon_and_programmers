def solution(n):
    if 1 <= n <= 99:
        return n
    else:
        total = 99
        for i in range(100, n + 1):
            if i % 100 // 10 - i % 10 == i // 100 - i % 100 // 10:
                total += 1
        return total


print(solution(int(input())))